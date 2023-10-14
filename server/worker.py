from server.core.celery import get_worker

app = get_worker()

__all__ = ("app",)
