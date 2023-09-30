from pydantic_settings import BaseSettings
from functools import cache
from pathlib import Path


class Settings(BaseSettings):
    # APP
    APP_NAME: str = "crm_parceiro"
    APP_VERSION: str = "v0.1.0"

    # TEMPLATES E ESTATICOS
    TEMPLATE_FOLDER: str = str(Path("./apps/pages"))
    STATIC_FOLDER: str = str(Path("./static/public"))
    STATIC_URL_PATH: str = "/static"


@cache
def get_config() -> Settings:
    return Settings()
