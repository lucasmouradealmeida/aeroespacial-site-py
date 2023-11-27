import logging

from flask import Flask

logger = logging.getLogger(__name__)


def init_app(app: Flask):
    """Registrar Blueprints de rotas REST.

    Args:
        app (Flask): Instancia do Flask.
    """
    try:
        from server.controllers import (
            home_controller,
            login_controller,
        )

        app.register_blueprint(home_controller.bp)
        app.register_blueprint(login_controller.bp)

    except Exception as err:
        logger.error(err, exc_info=True)
        raise err


__all__ = ("init_app",)
