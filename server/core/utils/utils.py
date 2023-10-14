from typing import Any, Callable


def getcall(*funcs: Callable[[], Any], no_except: bool = False) -> Any:
    res = None
    for func in funcs:
        try:
            if callable(func) and (res := func()) is not None:
                break
        except Exception as err:
            if no_except is False:
                raise err
    return res


def get_or_none(target: Callable, *args, **kwargs) -> Any:
    try:
        res = target(*args, **kwargs)
        return res if res else None
    except BaseException:
        return None
