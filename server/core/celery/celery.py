from functools import cache

from celery import Celery

from server.config import get_config
from server.registers import scheduler, tasks


def create_app() -> Celery:
    config = get_config()
    configure = {
        "task_serializer": config.CELERY_TASK_SERIALIZER,
        "accept_content": config.CELERY_ACCEPT_CONTENT,
        "result_serializer": config.CELERY_RESULT_SERIALIZER,
        "result_backend": config.CELERY_BACKEND_URL,
        "timezone": config.CELERY_TIMEZONE,
        "broker_url": config.CELERY_BROKER_URL,
        "task_queues": config.CELERY_TASK_QUEUES,
        "task_default_queue": config.CELERY_QUEUE_DEFAULT,
        "task_create_missing_queues": config.CELERY_TASK_CREATE_MISSING_QUEUES,
        "broker_transport_options": {
            "visibility_timeout": config.CELERY_VISIBILITY_TIMEOUT
        },
        "result_backend_transport_options": {
            "result_chord_ordered": True,
            "result_expires": config.CELERY_RESULT_TIMEOUT,
        },
        "broker_connection_retry_on_startup": True,
        "worker_prefetch_multiplier": 1,
        "task_track_started": True,
    }
    app = Celery(config.APP_NAME)
    app.conf.update(**configure)
    return app


@cache
def get_app() -> Celery:
    return create_app()


def get_worker() -> Celery:
    app = get_app()
    tasks.init_app(app)
    scheduler.init_app(app)
    return app


__all__ = ("create_app", "get_app", "get_worker")
