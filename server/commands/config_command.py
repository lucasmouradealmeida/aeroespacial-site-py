from typing import Any, TypeVar

from flask import Blueprint
from rich import print_json

from server.config import get_config

T = TypeVar("T")


def cls_to_dict(cls_: T) -> dict[str, Any]:
    return dict(
        (key, getattr(cls_, key))
        for key in dir(cls_)
        if not (
            key.startswith("_")
            or key.startswith("model_")
            or callable(getattr(cls_, key))
        )
    )


bp = Blueprint("config_cli", __name__, cli_group="config")
bp.cli.help = "Ferramentas de configurações da aplicação."


@bp.cli.command("show", help="Visualizar configurações da aplicação.")
def config_show():
    config = get_config()
    config_dict = cls_to_dict(config)
    print_json(data=config_dict, default=str)
