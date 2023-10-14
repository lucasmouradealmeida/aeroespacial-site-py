"""Exemplo:

class UpdatedItem(Item, metaclass=AllOptionalMeta):
    pass

"""
from __future__ import annotations

from typing import Any, Dict, Optional, Tuple

from pydantic.main import BaseModel, _model_construction


class AllOptionalMeta(_model_construction.ModelMetaclass):
    def __new__(
        self, name: str, bases: Tuple[type], namespaces: Dict[str, Any], **kwargs
    ):
        annotations = namespaces.get("__annotations__", {})
        for base in bases:
            for base_ in base.__mro__:
                if base_ is BaseModel:
                    break
                annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith("__"):
                annotations[field] = Optional[annotations[field]]
        namespaces["__annotations__"] = annotations
        return super().__new__(self, name, bases, namespaces, **kwargs)


__all__ = ("AllOptionalMeta",)
