from django.core.management.base import BaseCommand
from rooms import models as rooms_models


class Command(BaseCommand):
    
    help = "This command write name to Amenity Model."

    def handle(self, *args, **options):
        amenities = [
            "주방",
            "샴푸",
            "난방",
            "에어컨",
            "무선 ",
            "옷걸이",
            "다리미",
            "헤어드",
            "노트북",
            "TV",
            "욕실",
        ]
        for a in amenities:
            rooms_models.Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))