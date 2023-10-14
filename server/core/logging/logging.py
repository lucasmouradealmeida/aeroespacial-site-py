import logging


def get_logger(*args, **kwargs) -> logging.Logger:
    """Get Custom Logger.

    Args:
        log_level (str, optional): Log level.
                   Defaults to "%(asctime)s - %(name)s - %(levelname)s - %(message)s".
        format (int, optional): Date format. Defaults to logging.INFO.

    Returns:
        logging.Logger:
    """
    from server.config import get_config

    config = get_config()
    logger_level: int = kwargs.pop("log_level", logging.INFO)
    format: str = kwargs.pop(
        "format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    if hasattr(logging, config.LOG_LEVEL):
        logger_level = getattr(logging, config.LOG_LEVEL)
    logger = logging.getLogger(*args, **kwargs)
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(format))
    ch.setLevel(logger_level)
    logger.addHandler(ch)
    logger.setLevel(logger_level)
    return logger
