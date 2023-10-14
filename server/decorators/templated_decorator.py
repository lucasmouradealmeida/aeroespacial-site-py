from functools import wraps
from typing import Callable, Optional

from flask import render_template, request

from server.core.context import Context


def templated(template: Optional[str] = None):
    def decorator(f: Callable):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = f"{request.endpoint.replace('.', '/')}.html"
            ctx = Context.from_request(request)
            res = f(ctx, *args, **kwargs)
            if res is None:
                res = {}
            elif not isinstance(res, dict):
                return res
            res["ctx"] = ctx
            return render_template(template_name, **res)

        return decorated_function

    return decorator
