from __future__ import annotations

import typing as t

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ValidationError

from ..utils import camel_to_snake, snake_to_camel, to_camel

M = t.TypeVar("M", bound="BaseModel")


def to_class(class_: t.Type[M], dict_: dict, to_snakecase: bool) -> M:
    return class_(**(camel_to_snake(dict_) if to_snakecase else dict_))


class BaseModelConfig:
    arbitrary_types_allowed = True
    alias_generator = to_camel
    populate_by_name = True


class BaseModel(PydanticBaseModel):
    class Config(BaseModelConfig):
        pass

    def _get_props(self) -> list[str]:
        """
        Retorna atributos da classe que são decorators de property

        Returns:
            list[str]: Lista de atributos
        """
        return [x for x in dir(self.__class__) if isinstance(getattr(self.__class__, x), property)]

    def dict(self, *args, **kwargs) -> t.Dict[str, t.Any]:
        """Metodo Pydantic.BaseModel.dict.

        Args:
            to_camelcase (bool, optional): Converter nome dos campos de snake_case
                                           para camelCase. Defaults to False.
            add_property_decors (bool, optional): Adicionar os campos marcados
                                           com @property. Defaults to False.

        Returns:
            Dict[str, Any]: Retorna a classe no formato de dicionario.
        """
        to_camelcase = kwargs.pop("to_camelcase", False)
        add_property_decors = kwargs.pop("add_property_decors", False)

        d = super().dict(*args, **kwargs)

        if add_property_decors:
            atributos = self._get_props()
            for atr in atributos:
                d[atr] = getattr(self, atr)

        if to_camelcase:
            d = snake_to_camel(d)

        return d

    def to_dict(self, *args, **kwargs) -> t.Dict[str, t.Any]:
        """Metodo Transformar classe em dict.

        Returns:
            Dict[str, Any]: Retorna a classe no formato de dicionario.
        """
        return self.dict(*args, **kwargs)

    @classmethod
    def from_dict(cls: t.Type[M], d: t.Dict[str, t.Any], to_snakecase: bool = False) -> M:
        """Criar Classe a partir de um dicionario.

        Args:
            d (Dict[str, Any]): Dicionario de dados.

        Returns:
            M: Model instanciada.
        """
        return to_class(class_=cls, dict_=d, to_snakecase=to_snakecase)

    @classmethod
    def from_collection(cls: t.Type[M], ld: t.List[t.Dict[str, t.Any]], to_snakecase: bool = False) -> t.List[M]:
        """Criar Classe a partir de um dicionario.

        Args:
            ld (List[Dict[str, Any]]): Lista de dicionario de dados.

        Returns:
            List[M]: lista de models instanciada.
        """
        return [to_class(class_=cls, dict_=d, to_snakecase=to_snakecase) for d in ld]

    @classmethod
    def new(cls, **kwargs) -> t.Tuple[t.Union[M, None], t.Union[ValidationError, None]]:
        """Instanciar a classe retornando a lista de erros.

        Returns:
            Tuple[Union[M, None], Union[ValidationError, None]]: retorna o erro
            (se houver) e a classe instanciada (se puder).
        """
        error: t.Union[t.Any, ValidationError] = None
        instance: t.Union[t.Any, None] = None
        try:
            instance = cls.from_dict(kwargs, to_snakecase=True)
        except ValidationError as e:
            error = e
        return instance, error


__all__ = (
    "BaseModel",
    "BaseModelConfig",
)
