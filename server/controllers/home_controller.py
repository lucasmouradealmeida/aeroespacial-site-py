from flask import Blueprint

from server.core.context import Context
from server.decorators import with_context

bp = Blueprint("home", __name__)


@bp.route("/", methods=["GET"], endpoint="home")
@with_context(template="./home.html")
def home_controller(ctx: Context):
    return {"titulo": "Home"}
