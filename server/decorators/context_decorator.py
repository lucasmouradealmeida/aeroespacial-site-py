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
