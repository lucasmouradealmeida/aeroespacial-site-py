from flask import Flask
from server.register import register
from server.config import get_config


def create_app() -> Flask:
    config = get_config()

    app = Flask(
        config.APP_NAME,
        template_folder=config.TEMPLATE_FOLDER,
        static_folder=config.STATIC_FOLDER,
        static_url_path=config.STATIC_URL_PATH,
    )

    register.init_app(app)
    return app
