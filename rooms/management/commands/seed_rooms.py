import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models
from django.contrib.admin.utils import flatten #2arrays ->1array

class Command(BaseCommand):
    
    help = "This command create many rooms"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int, help="How many rooms you want to create")

    def handle(self, *args, **options):
        number = options.get("number")
        
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        room_seeder = Seed.seeder()
        room_seeder.add_entity(room_models.Room, number, {
            "name": lambda x: room_seeder.faker.address(), # I tried to make shorter text (avoid too long text)
            "host": lambda x: random.choice(all_users),
            "room_type": lambda x: random.choice(room_types),
            "guests": lambda x: random.randint(1,20),
            "price": lambda x: random.randint(1,300),
            "beds": lambda x: random.randint(1,5),
            "bedrooms": lambda x: random.randint(1,5),
            "baths": lambda x: random.randint(1,5),
        })
        inserted_rooms = room_seeder.execute()
        inserted_clean = flatten(list(inserted_rooms.values()))
        for pk in inserted_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(1, random.randint(7,14)):
                room_models.Photo.objects.create(
                    caption = room_seeder.faker.sentence(),
                    file = f"room_photos/{random.randint(1,31)}.webp",
                    room = room
                )
        
            for a in amenities:
                magic_number = random.randint(0,15)
                if magic_number % 2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0,15)
                if magic_number % 2 == 0:
                    room.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0,15)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)        
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))