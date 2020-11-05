from telegram.ext import CommandHandler

from apps.bot import callbacks


classes = [
    CommandHandler('start', callbacks.start)
]
