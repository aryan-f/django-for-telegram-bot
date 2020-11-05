from apps.bot.management.commands.runbot import updater


def call_bot_method(method_name, *args, **kwargs):
    method = getattr(updater.bot, method_name)
    method(*args, **kwargs)
