from django.core.management.base import BaseCommand, CommandError

from main.views import get_and_create_data


class Command(BaseCommand):
    help = "Gets the laptop from jumia"

    def handle(self, *args, **options):
        x = get_and_create_data()
        self.stdout.write(self.style.SUCCESS("Successfully gotten the data and saved to db"))
