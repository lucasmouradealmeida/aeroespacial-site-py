import logging

from flask import Flask

logger = logging.getLogger(__name__)


def init_app(app: Flask):
    """Registrar Blueprints de rotas.

    Args:
        app (Flask): Instancia do Flask.
    """
    try:
        from server.routes import (
            home
        )

        app.register_blueprint(home.bp)

    except Exception as err:
        logger.error(err, exc_info=True)
        raise err


__all__ = ("init_app",)
