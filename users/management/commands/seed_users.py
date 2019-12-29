from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models


class Command(BaseCommand):
    
    help = "This command create many users"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int, help="How many users you want to create")

    def handle(self, *args, **options):
        number = options.get("number")
        print(number)
        user_seeder = Seed.seeder()
        user_seeder.add_entity(user_models.User, number, {
            "is_staff": False,
            "is_superuser": False,
        })
        user_seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))