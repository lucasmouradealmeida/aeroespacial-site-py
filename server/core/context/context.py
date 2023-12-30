from __future__ import annotations

from typing import Any, Optional, Union

from flask import Request, session
from pydantic import BaseModel, ConfigDict, PrivateAttr

from server.config import Settings, get_config
from server.core.exceptions import UserNotFoundError

model_config = ConfigDict(arbitrary_types_allowed=True)


class Context(BaseModel):
    """Contexto da execução."""

    model_config = model_config

    _token: str = ""
    _internal_token: str = ""
    _is_request: bool = False
    _is_background: bool = False
    _scopes: list[str] = PrivateAttr(default_factory=list)

    headers: dict[str, str] = {}
    request: Union[Request, None] = None
    id_pessoa: Union[int, None] = None

    def __init__(self, **data):
        user = data.pop("user", None)
        token = data.pop("token", "")
        is_request = data.pop("is_request", False)
        is_background = data.pop("is_background", False)

        super().__init__(**data)
        self._user = user
        self._token = token
        self._is_request = is_request
        self._is_background = is_background
        if self._is_request is False and self._is_background is False:
            self._is_background = True
        if not self.id_pessoa and self._user:
            self.id_pessoa = self._user.id_pessoa


    @property
    def config(self) -> Settings:
        """Configurações

        Returns:
            Settings: Atributos da configuração.
        """
        return get_config()

    @property
    def token(self) -> str:
        """Obter o Apê11 token.

        Raises:
            TokenRequiredError: É requerido o token para execução.

        Returns:
            str: Token.
        """

        return

    @property
    def internal_token(self) -> str:
        """Obter o token interno.

        Raises:
            TokenRequiredError: É requerido o token para execução.

        Returns:
            str: Token.
        """

        return

    @property
    def token_parceiro(self) -> str:
        """Obter o token do parceiro Apê11.

        Raises:
            TokenRequiredError: É requerido o token para execução.

        Returns:
            str: Token.
        """

        return

    @property
    def is_logged(self) -> bool:
        """Usuario esta logado?

        Returns:
            bool: True se sim.
        """
        try:
            return bool(session.get("email"))
        except BaseException:
            return False

    @property
    def scopes(self) -> list[str]:
        # if self._scopes:
        #     self._scopes = []
        return self._scopes

    @classmethod
    def from_request(cls, r: Request) -> Context:
        """Criar classe de contexto em cima dos dados da request.

        Args:
            r (Optional[Request]): Dados da request. Default is None.
            env (str): Ambiente de execução. Default is 'prd'.
            user (Optional[Pessoa]): Dados da pessoa. Default is None

        Returns:
            Context: Dados de contexto.
        """
        context: dict[str, Any] = {}
        context["is_request"] = True
        context["request"] = r
        context["headers"] = dict(r.headers)
        return cls(**context)


__all__ = ("Context",)
