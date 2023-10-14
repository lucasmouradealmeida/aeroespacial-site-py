import logging

from flask import Flask

logger = logging.getLogger(__name__)


def init_app(app: Flask):
    """Registrar Blueprints de comandos.

    Args:
        app (Flask): Instancia do Flask.
    """
    try:
        from server.commands import config_command

        app.register_blueprint(config_command.bp)

    except Exception as err:
        logger.error(err, exc_info=True)
        raise err


__all__ = ("init_app",)
