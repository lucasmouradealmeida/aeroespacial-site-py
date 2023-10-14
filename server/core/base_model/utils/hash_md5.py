import hashlib
import json
import typing as t

from server.core import logging

from .utils import sort_dict

T = t.TypeVar("T")

logger = logging.getLogger(__name__)


def hash_md5(d: t.Union[T, t.Dict[t.Any, t.Any]]) -> str:
    """Gerar hash da classe.

    Returns:
        str: Hash.
    """
    if not (
        isinstance(d, dict) or (hasattr(d, "dict") and callable(getattr(d, "dict")))
    ):
        message_error = "Argumento de entrada invalido"
        logger.error(message_error, exc_info=True)
        raise Exception(message_error)

    dict_ = d if isinstance(d, dict) else d.dict()
    dict_str = json.dumps(sort_dict(dict_), default=str, indent=2)
    return hashlib.md5(dict_str.encode()).hexdigest()
