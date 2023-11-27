from __future__ import annotations

from typing import Any, Optional, Union

from flask import Request, session
from pydantic import BaseModel, ConfigDict, PrivateAttr

from server.config import Settings, get_config
from server.core.exceptions import ParceiroNotFoundError, UserNotFoundError
from server.models.parceiro_model import Parceiro
from server.models.pessoa_model import Pessoa

model_config = ConfigDict(arbitrary_types_allowed=True)


class Context(BaseModel):
    """Contexto da execução."""

    model_config = model_config

    _user: Union[Pessoa, None] = None
    _parceiro: Union[Parceiro, None] = None
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
    def parceiro(self) -> Parceiro:
        """Dados do parceiro

        Raises:
            ParceiroNotFoundError: Quando parceiro não for encontrado.

        Returns:
            Parceiro: Dados do parceiro.
        """

        return

    @property
    def view(self) -> dict[str, Any]:
        """Obter configurações visuais do parceiro.

        Returns:
            dict[str, Any]: Configurações visuais do parceiro.
        """
        return self.parceiro.configuracao

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
    def user(self) -> Pessoa:
        """Obter dados do usuario.
           O 'user' da execução contem os dados da pessoa na Apê11 obtida
           através do token.

        Raises:
            UserNotFoundError: Quando usuario não for encontrado.

        Returns:
            Pessoa: Dados da pessoa.
        """
        if self._user:
            return self._user

        elif self.id_pessoa:
            from server.services.pessoa_service import pessoa_service as pessoa_service

            self._user = pessoa_service.obter_pessoa(self, self.id_pessoa)
            return self._user
        else:
            raise UserNotFoundError("Usar o property 'is_logged' para verificar antes de obter o usuario!")

    @property
    def scopes(self) -> list[str]:
        # if self._scopes:
        #     self._scopes = []
        return self._scopes

    @classmethod
    def from_request(cls, r: Request, user: Optional[Pessoa] = None) -> Context:
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
        context["id_pessoa"] = None
        context["user"] = user
        return cls(**context)

    @classmethod
    def from_background(
        cls,
        id_pessoa: Optional[int] = None,
        user: Optional[Pessoa] = None,
    ) -> Context:
        """Criar classe de contexto de backend.

        Args:
            env (str): Ambiente de execução. Default is 'prd'.
            id_tarefa (Optional[int]): Id da tarefa. Default is None.
            id_pessoa (Optional[int]): Id pessoa. Default is None.
            user (Optional[Pessoa]): Usuario. Default is None.

        Returns:
            Context: Dados de contexto.
        """
        context: dict[str, Any] = {}
        context["is_background"] = True
        context["id_pessoa"] = id_pessoa
        context["user"] = user
        return cls(**context)


__all__ = ("Context",)
