from functools import cache


@cache
def create_key(name: str, *args, **kwargs) -> str:
    from server.core.context import Context

    keys = []
    for arg in args:
        if isinstance(arg, Context):
            continue
        keys.append(str(arg))
    for k, v in kwargs.items():
        if isinstance(v, Context):
            continue
        keys.append(f"{k!s}={v!s}")
    return f"{name}:" + "&".join(keys)


__all__ = ("create_key",)
