from django.core.management.base import BaseCommand
from core.bot import bot


class Command(BaseCommand):
    help = "Start the Telegram Bot Server"

    def handle(self, *args, **options):
        bot.infinity_polling()
