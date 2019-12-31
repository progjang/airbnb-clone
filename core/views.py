from django.shortcuts import render
from datetime import datetime
from rooms import models as room_models
# Create your views here.


def all_rooms(request):
    rooms = room_models.Room.objects.all()
    return render(request, "core/home.html", context={
        "rooms": rooms
    })