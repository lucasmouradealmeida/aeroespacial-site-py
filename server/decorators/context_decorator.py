import base64
from datetime import datetime, timedelta
from functools import wraps
from http import HTTPStatus
from typing import Callable, Optional, Union

from flask import (
    Response,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from pydash import _ as py_

from server.config import get_config
from server.core import logging
from server.core.context import Context
from server.services.token_service import token_service


def autenticador(ctx: Context, email: Union[str, None], senha: Union[str, None]) -> str:
    try:
        # token = token_service.login(
        #     ctx,
        #     username=email,
        #     password=base64.b64encode(bytes(senha, "utf-8")).decode("utf-8"),
        # )
        return
    except Exception as error:
        logging.get_logger(__name__).warning(error, exc_info=True)
        return None


def is_logged(ctx: Context, template) -> bool:
    permitted = ["index", "login"]
    if ctx.is_logged:
        return True
    else:
        for item in permitted:
            if item in template:
                return True
    return False


def check_session_expiry() -> bool:
    expire_at = session.get("expire_at")
    if expire_at and datetime.now() >= expire_at:
        # A sessão expirou
        return True
    else:
        # Faz o refresh da sessão e extende o periodo por mais 30 minutos
        session["expire_at"] = datetime.now() + timedelta(seconds=1800)
        return False


def has_permission(scope: Union[Callable, str], user_scopes: list[str]) -> bool:
    try:
        if isinstance(scope, str):
            return bool(scope in user_scopes)
        return bool(scope(user_scopes))
    except Exception as err:
        logging.get_logger(__name__).warning(err, exc_info=True)
        return False


def with_context(
    template: Optional[str] = None,
    scope: Union[str, Callable, None] = None,
    redirect_for: Union[str, None] = None,
):
    def decorator(f: Callable):
        @wraps(f)
        def decorated_function(*args, **kwargs) -> Response:
            ctx = Context.from_request(request)
            if scope and has_permission(scope, ctx.scopes) is False:
                if template:
                    config = get_config()
                    return redirect(url_for(redirect_for or config.PAGE_NOT_PERMISSION_REDIRECT))
                else:
                    return Response(status=HTTPStatus.FORBIDDEN)
            res = f(ctx, *args, **kwargs)
            if template:
                # Verifica o tempo da sessão do login
                if check_session_expiry():
                    session.clear()
                # Verifica se usuário tem permissão de acesso
                if is_logged(ctx, template) is False:
                    return redirect(url_for("home.home"))
                # Redireciona para outra página (uso do redirect)
                if py_.get(res, "location", None):
                    return redirect(res.location)
                # Redireciona para a página solicitada
                if not (res and isinstance(res, dict)):
                    res = {}
                res["ctx"] = ctx
                res = make_response(render_template(template, **res))
            return res

        return decorated_function

    return decorator


__all__ = ("with_context",)
