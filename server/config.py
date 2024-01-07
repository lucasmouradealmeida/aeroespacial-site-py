import locale
import os
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
    APP_NAME: str = "aeroespacial"
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
    LOG_FORMAT: str = str(os.getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

    # TOKEN SERVICE
    USER_SERVICE_TOKEN_EXPIRE: int = 60 * 60  # 1 hora
    TOKEN_EXPIRE: int = 60 * 60  # 1 hora
    UNLOGGED_LOGIN: str = ""

    # WEB
    # SESSION_SECRET: str = os.getenv(
    #     "SESSION_SECRET", "47a9d370f17f69a542227d02a7ce8e2c9114168cfddc17eae7bc807818e2e58e"
    # )
    PAGE_NOT_FOUND_REDIRECT: str = "home.home"
    PAGE_NOT_FOUND_MESSAGE: str = "Pagina não encontrada!"
    PAGE_NOT_PERMISSION_REDIRECT: str = "home.home"

  
    # # CACHE - REDIS
    # REDIS_URL: str = getcall(
    #     lambda: os.getenv("APP_CACHE_URL"),
    #     lambda: "redis://localhost:6379/0",
    #     no_except=True,
    # )

    # # CACHE - REDIS
    # SESSION_URL: str = getcall(
    #     lambda: os.getenv("APP_SESSION_URL"),
    #     lambda: "redis://localhost:6379/1",
    #     no_except=True,
    # )

    # # CELERY
    # CELERY_BROKER_URL: str = getcall(
    #     lambda: os.getenv("APP_BROKER_URL"),
    #     lambda: "redis://localhost:6379/2",
    #     no_except=True,
    # )

    # CELERY_BACKEND_URL: str = getcall(
    #     lambda: os.getenv("APP_BACKEND_URL"),
    #     lambda: "redis://localhost:6379/2",
    #     no_except=True,
    # )

    # CELERY_TASKS_FOLDER: str = "server.tasks"
    # CELERY_QUEUE_DEFAULT: str = "crm_parceiro_queue_1"
    # CELERY_TASK_QUEUES: list[Queue] = [Queue("crm_parceiro_queue_1")]
    # CELERY_TASK_SERIALIZER: str = "json"
    # CELERY_RESULT_SERIALIZER: str = "json"
    # CELERY_ACCEPT_CONTENT: list[str] = ["json"]
    # CELERY_TIMEZONE: str = os.getenv("TZ", "America/Sao_Paulo")
    # CELERY_TASK_CREATE_MISSING_QUEUES: bool = True
    # CELERY_VISIBILITY_TIMEOUT: int = 432000
    # CELERY_RESULT_TIMEOUT: int = 432000

    # CACHE
    CACHE_PARCEIRO_EXPIRE: int = 12 * 60 * 60  # 12 horas

    CACHE_TOKEN_EXPIRE: int = 10 * 60  # 10 minutos
    CACHE_USUARIO_EXPIRE: int = 12 * 60  # 12 horas

    # SESSION
    # SESSION_TYPE: str = "redis"
    SESSION_PERMANENT: bool = True  # Sessão permanente (12 horas)
    SESSION_LIFETIME: int = 12 * 3600  # Duração da sessão (12 horas)
    SESSION_REFRESH_REQUEST: bool = True  # Atualiza a sessão a cada solicitação para estender o tempo de inatividade
    SESSION_REFRESH_SECONDS: int = 1800  # Tempo de atualização personalizado em segundos (30 minutos)
    SESSION_USE_SIGNER: bool = True  # Usar assinatura de sessão para segurança
    SESSION_COOKIE_NAME: str = "aeroespacial"  # Nome da sessão para segurança

    if IS_DEV_MODE:
        SESSION_COOKIE_SECURE: bool = False
        SESSION_COOKIE_HTTPONLY: bool = False
    else:
        SESSION_COOKIE_SECURE: bool = False
        SESSION_COOKIE_HTTPONLY: bool = False


@cache
def get_config() -> Settings:
    return Settings(AMBIENTE=AMBIENTE)
