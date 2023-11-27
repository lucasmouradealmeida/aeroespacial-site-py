import os
from typing import List

from celery import Celery

from server.config import get_config

folders_invalid = ("__pycache__", "test", "tests")


def init_app(app: Celery):
    """Registrando tarefas no Celery.

    Args:
        app (Celery): Instancia do Celery.
    """
    config = get_config()
    app.autodiscover_tasks(packages=task_scan(config.CELERY_TASKS_FOLDER))


def task_scan(task_path: str) -> List[str]:
    """Scanear tasks.

    Returns:
        List[str]: Lista de tasks
    """
    task_folder = task_path
    task_dir = os.path.join(os.getcwd(), *task_folder.split("."))

    tasks = []
    for dirpath, _, filenames in os.walk(task_dir):
        valid = True
        for fi in folders_invalid:
            if fi in dirpath:
                valid = False
                break
        if valid:
            for f in filenames:
                if f.startswith("__") or f.endswith(".pyc") or not f.endswith(".py"):
                    continue
                tasks.append(task_folder + "." + f[:-3])

    return tasks


__all__ = ("init_app",)
