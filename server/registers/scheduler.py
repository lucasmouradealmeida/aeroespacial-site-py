from celery import Celery
from celery.schedules import crontab


def init_app(app: Celery):
    """Registrando tarefas no Celery Beat Scheduler.

    Args:
        app (Celery): Instancia do Celery.
    """
    schedule: dict[str, dict] = {
        "task_healthcheck": {
            "task": "task_healthcheck",
            "schedule": crontab(minute="*/5"),
        },
    }

    if schedule:
        app.conf.beat_schedule = schedule


__all__ = ("init_app",)
