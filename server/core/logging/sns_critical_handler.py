import logging
import os
from distutils.util import strtobool

import boto3

from server.config import get_config

config = get_config()

if strtobool(os.getenv("SNS_TOPIC_ERROR_FAKE", "0")):
    from unittest.mock import MagicMock

    sns = MagicMock()

else:
    sns = boto3.client("sns", region_name="us-east-1")


class TopicHandler(logging.StreamHandler):
    """Classe Handler de envio de mensagens de erro ao SNS"""

    def __init__(self):
        """Construtor"""
        logging.StreamHandler.__init__(self)
        self._name = config.APP_NAME
        self._ambiente = config.AMBIENTE
        self._subtitle = f"[AWS_ERRO][{self._ambiente}] {self._name}"

    def emit(self, record):
        """Envia mensagem para o Topico"""
        msg = self.format(record)
        message = f"Erro na aplicação {self._name}:\n---\n{msg}\n---"
        sns.publish(
            TopicArn=config.SNS_TOPIC_ERROR,
            Subject=self._subtitle,
            Message=message,
        )


sns_critical_handler = TopicHandler()
sns_critical_handler.setLevel(logging.CRITICAL)


__all__ = (
    "TopicHandler",
    "sns_critical_handler",
)
