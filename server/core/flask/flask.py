from http import HTTPStatus

from flask import Flask, flash, redirect, url_for
from flask_session import Session
from flask_wtf.csrf import CSRFProtect

from server.config import get_config
from server.registers import commands, routes


def create_app() -> Flask:
    config = get_config()
    csrf = CSRFProtect()

    app = Flask(
        config.APP_NAME,
        template_folder=config.TEMPLATE_FOLDER,
        static_folder=config.STATIC_FOLDER,
        static_url_path=config.STATIC_URL_PATH,
    )
    app.secret_key = config.SESSION_SECRET

    # Configuração do Flask-Session
    # app.config["SESSION_TYPE"] = config.SESSION_TYPE
    app.config["SESSION_PERMANENT"] = config.SESSION_PERMANENT
    app.config["PERMANENT_SESSION_LIFETIME"] = config.SESSION_LIFETIME
    app.config["SESSION_REFRESH_EACH_REQUEST"] = config.SESSION_REFRESH_REQUEST
    app.config["SESSION_REFRESH_EACH_SECONDS"] = config.SESSION_REFRESH_SECONDS
    app.config["SESSION_USE_SIGNER"] = config.SESSION_USE_SIGNER
    app.config["SESSION_COOKIE_NAME"] = config.SESSION_COOKIE_NAME
    app.config["SESSION_COOKIE_SECURE"] = config.SESSION_COOKIE_SECURE
    app.config["SESSION_COOKIE_HTTPONLY"] = config.SESSION_COOKIE_HTTPONLY

    @app.errorhandler(HTTPStatus.NOT_FOUND)
    def not_found(e):
        flash(config.PAGE_NOT_FOUND_MESSAGE, "error")
        return redirect(url_for(config.PAGE_NOT_FOUND_REDIRECT))

    routes.init_app(app)
    commands.init_app(app)
    csrf.init_app(app)
    Session(app)
    return app
