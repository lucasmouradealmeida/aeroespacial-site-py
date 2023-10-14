from __future__ import annotations

import json
from typing import Any, Dict, Generator, Tuple, Union

from pydantic import BaseModel


def hstore_value(v: Any) -> Union[str, None]:
    if v is None:
        return v
    return v if isinstance(v, str) else json.dumps(v, default=str)


class HStore(BaseModel):
    _hs: Dict[str, Union[str, None]]

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__()
        self._hs = {}
        input_init = {}
        for arg in args:
            if isinstance(arg, dict):
                input_init.update(arg)
        for k, v in kwargs.items():
            input_init.update({k: v})
        for k, v in input_init.items():
            self._hs[k] = hstore_value(v)

    def __getitem__(self, name: str) -> Union[str, None]:
        if not self._hs:
            return None
        return self._hs.get(name)

    def __setitem__(self, name: str, value: Any) -> None:
        if not self._hs:
            self._hs = {}
        self._hs[name] = hstore_value(value)

    def dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return self._hs

    def to_dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return self.dict(*args, **kwargs)

    def __iter__(self) -> Generator[Tuple[str, Any], None, None]:
        yield from self._hs.items()

    # def __dict__(self) -> Dict[str, Any]:
    #     return self._hs

    def __str__(self) -> str:
        return json.dumps(self._hs)

    def __repr__(self) -> str:
        return self.__str__()


hstore = HStore


__all__ = ("HStore", "hstore")
