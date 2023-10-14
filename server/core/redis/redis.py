from functools import lru_cache

from redis import Redis


def create_conn(host: str, port: str = "6379", db: str = "0") -> Redis:
    r = Redis(
        host=host,
        port=port,
        db=db,
        decode_responses=True,
    )
    return r


@lru_cache()
def get_conn() -> Redis:
    from server.config import get_config

    config = get_config()
    return create_conn(host=config.REDIS_HOST, port=config.REDIS_PORT, db="2")
