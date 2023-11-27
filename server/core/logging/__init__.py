from .logging import get_logger
from .sns_critical_handler import sns_critical_handler

getLogger = get_logger

__all__ = (
    "get_logger",
    "sns_critical_handler",
    "getLogger",
)
