from django.conf import settings
from telegram.ext import Updater as BaseUpdater


class Updater(BaseUpdater):

    def __init__(self):
        super().__init__(**settings.TELEGRAM_BOT)
