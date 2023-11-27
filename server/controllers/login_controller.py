from datetime import datetime, timedelta

from flask import Blueprint, redirect, request, session, url_for

from server.core.context import Context
from server.decorators import with_context
from server.decorators.context_decorator import autenticador

bp = Blueprint("login", __name__)


@bp.route("/login", methods=["GET", "POST"], endpoint="login")
@with_context(template="./login.html")
def login_controller(ctx: Context):
    if ctx.is_logged:
        return redirect(url_for("dashboard.dashboard"))
    if request.method == "POST":
        # get_usuario = autenticador(ctx, request.form["email"], request.form["password"])
        get_usuario = "admin"
        if get_usuario is not None:
            session["expire_at"] = datetime.now() + timedelta(seconds=1800)
            session["email"] = request.form["email"]
            return redirect(url_for("dashboard.dashboard"))
        return {"bad_login": "Usuário ou senha estão incorretos."}
    return


@bp.route("/recuperar-senha", methods=["GET"], endpoint="recuperar")
@with_context(template="./recuperar-senha.html")
def recuperar_senha_controller(ctx: Context):
    return {"titulo": "Recuperar Senha"}


@bp.route("/confirmar-senha", methods=["GET"], endpoint="confirmar")
@with_context(template="./confirmar-senha.html")
def confirmar_senha_controller(ctx: Context):
    return {"titulo": "Confirmar Senha"}


@bp.route("/logout", methods=["GET"], endpoint="logout")
@with_context()
def logout_controller(ctx: Context):
    session.clear()
    return redirect(url_for("home.home"))
