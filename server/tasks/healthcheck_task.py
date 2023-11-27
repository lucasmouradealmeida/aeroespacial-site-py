from server.core import logging
from server.core.celery import get_app

logger = logging.get_logger(__name__)
app = get_app()


@app.task(name="task_healthcheck", bind=True)
def task_healthcheck(self):
    try:
        msg = f"ping: {self.request.id}"
        logger.info(msg)
        # return msg

    except Exception as err:
        logger.error(str(err), exc_info=True)
        raise err
