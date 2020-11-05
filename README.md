# Python Telegram Bot on a Django Backend
This repository is a template for mixing the Django framework with the **Python Telegram Bot** library, allowing you to
create Telegram bots with a website, backed by Django. This often comes in handy, specially when you need to handle
financial transactions for the users of the bot.

# Getting Started

## Dependencies
The project uses **Django-Q** for the asynchronous tasks, which in my experience, are really useful. A `djangoadmin` 
command, by the name `runbot`, has been implemented, which sets up an updater for the Telegram bot and clusters for 
Django-Q in the same parent process, allowing them to communicate. Doing so allows you to call asynchronous tasks from
Django views to use the bot. An example routine has been implemented and placed in `apps.bot.tasks`, called 
`call_bot_method`, which can accept the name of a method of the `bot` object and call it with the provided arguments.
You can run the command below to install the needed dependencies:

```shell script
pip install -r requirements.txt
```

## Configuration
The configuration for the Updater for the Telegram bot has been placed in Django's `settings.py`. Django-Q is set up to
use Redis as its in-memory database engine. Some of the settings have been moved to `.env` for obvious reasons. I 
suggest that you move the settings for the database to this file as well, after switching to a better DBMS like 
PostgreSQL. The variables that need to be defined in `.env` are:

+ `DJANGO_SECRET_KEY`: The secret key for Django's functionalities.
+ `DJANGO_Q_WORKERS`: Number of clusters created for the asynchronous tasks.
+ `REDIS_HOST`: Host address for Redis.
+ `REDIS_PORT`: Port No. for Redis. 
+ `DJANGO_Q_REDIS_DB`: Redis database for Django-Q.
+ `TELEGRAM_BOT_TOKEN`: The token for your Telegram bot.
+ `TELEGRAM_BOT_WORKERS`: Number of workers created for handling the messages the bot receives.

## Deployment
You can find tutorials on how to deploy Django itself. As for the bot and `Django-Q`, an easy solution is to create a 
`systemd` service which executes the command below:

```shell script
python manage.py runbot
```

This command comes with an optional argument, `--bot-logging`, which specifies the logging level for the Python Telegram
Bot library. Refer to [this page](https://docs.python.org/3/library/logging.html#levels) for more info.