import base64
import locale
import os
import secrets
from distutils.util import strtobool as stb
from functools import cache
from pathlib import Path

from kombu import Queue
from pydantic_settings import BaseSettings

from server.core.utils.utils import getcall
from server.enums.ambiente_enum import AmbienteEnum

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def strtobool(v) -> bool:
    return bool(stb(v))


AMBIENTE = str(os.getenv("AMBIENTE")).lower()

class Settings(BaseSettings):
    # APP
    APP_NAME: str = "aeroespacial-site"
    APP_VERSION: str = "v1.0.0"
    APP_DOMAIN: str = "portal"

    # AMBIENTE
    AMBIENTE: AmbienteEnum
    TIMEZONE: str = os.getenv("TZ", "America/Sao_Paulo")
    IS_DEV_MODE: bool = strtobool(os.getenv("IS_DEV_MODE", "0"))

    # TEMPLATES E ESTATICOS
    TEMPLATE_FOLDER: str = str(Path("./client/pages"))
    STATIC_FOLDER: str = str(Path("./client/public"))
    STATIC_URL_PATH: str = "/static"

    # LOGGER
    LOG_LEVEL: str = str(os.getenv("LOG_LEVEL", "INFO")).upper()
    LOG_FORMAT: str = str(
        os.getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    # WEB
    SESSION_SECRET: str = secrets.token_hex()
    PAGE_NOT_FOUND_REDIRECT: str = "home.home"
    PAGE_NOT_FOUND_MESSAGE: str = "Pagina não encontrada!"
    PAGE_NOT_PERMISSION_REDIRECT: str = "home.home"

    # CACHE
    CACHE_PARCEIRO_EXPIRE: int = 12 * 60 * 60  # 12 horas
    CACHE_TOKEN_EXPIRE: int = 10 * 60  # 10 minutos
    CACHE_USUARIO_EXPIRE: int = 12 * 60  # 12 horas

    # SESSION
    SESSION_TYPE: str = "redis"
    SESSION_PERMANENT: bool = True  # Sessão permanente (12 horas)
    SESSION_LIFETIME: int = 12 * 3600  # Duração da sessão (12 horas)
    SESSION_REFRESH_REQUEST: bool = True  # Atualiza a sessão a cada solicitação para estender o tempo de inatividade
    SESSION_REFRESH_SECONDS: int = (
        1800  # Tempo de atualização personalizado em segundos (30 minutos)
    )
    SESSION_USE_SIGNER: bool = True  # Usar assinatura de sessão para segurança
    SESSION_COOKIE_NAME: str = "aeroespacial-site"  # Nome da sessão para segurança


@cache
def get_config() -> Settings:
    return Settings(AMBIENTE=AMBIENTE)
