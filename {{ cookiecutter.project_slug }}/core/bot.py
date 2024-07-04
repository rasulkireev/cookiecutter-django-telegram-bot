import telebot

from {{ cookiecutter.project_slug }}.settings import TELEGRAM_BOT_TOKEN
from core.utils import get_{{ cookiecutter.project_slug }}_logger

logger = get_{{ cookiecutter.project_slug }}_logger(__name__)

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['help'])
def send_help(message):
    logger.info(f"/help command requested", telegram_user_id=message.from_user.id)
    help_text = (
        "Here are the commands you can use:\n"
        "/help - Show this help message\n"
        "/start - Get a welcome message\n"
    )
    bot.reply_to(message, help_text)
    logger.info(f"/help command executed", telegram_user_id=message.from_user.id)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    logger.info(f"/start command requested", telegram_user_id=message.from_user.id)
    bot.reply_to(message, "Привет, как дела?")
    logger.info(f"/start command executed", telegram_user_id=message.from_user.id)
