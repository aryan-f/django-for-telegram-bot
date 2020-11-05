import logging
import signal

from django.core.management.base import BaseCommand
from django_q.cluster import Cluster
from apps.bot.updater import Updater

cluster = Cluster()
updater = Updater()


class Command(BaseCommand):
    help = 'Initiates the updater for the Telegram bot, as well as a cluster for Django-Q.'

    def add_arguments(self, parser):
        parser.add_argument('--bot-logging', type=int, default=30)

    def handle(self, *args, **options):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=options['bot_logging'])
        cluster.start()
        self.bind_signals()
        self.register_handlers()
        self.stderr.write('Initiating the Updater...')
        updater.start_polling()
        self.stderr.write('Listening for updates...')

    @classmethod
    def register_handlers(cls):
        from apps.bot import handlers
        for handler in handlers.classes:
            updater.dispatcher.add_handler(handler)

    # noinspection PyTypeChecker
    def bind_signals(self):
        signal.signal(signal.SIGINT, self.graceful_exit)
        signal.signal(signal.SIGTERM, self.graceful_exit)

    def graceful_exit(self, *args):
        self.stderr.write('Stopping the Updater...')
        updater.stop()
        cluster.stop()
