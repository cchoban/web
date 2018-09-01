import logging
import os
from django.conf import settings


class new:

    def __init__(self, message):
        self.message = message
        self.path = os.path.join(settings.BASE_DIR,"choban.log")
        logging.basicConfig(filename=self.path)

    def logError(self):
        logging.error(self.message)

    def logInfo(self):
        logging.info(self.message)
