import re
from functools import lru_cache
from urllib.parse import urlparse

from redis import Redis


def uri_to_conn(uri: str) -> tuple[str, str, str]:
    pu = urlparse(uri)
    host, port = pu.netloc.split(":")
    db = re.sub(r"^.*([0-9]+).*$", r"\1", pu.path) or "0"
    return host, port, db


def create_conn(host: str, port: str = "6379", db: str = "0", decoded_strings: bool = False) -> Redis:
    r = Redis(
        host=host,
        port=port,
        db=db,
        decode_responses=decoded_strings,
    )
    return r


@lru_cache()
def get_conn() -> Redis:
    from server.config import get_config

    config = get_config()
    host, port, db = uri_to_conn(config.REDIS_URL)
    return create_conn(host=host, port=port, db=db, decoded_strings=True)
