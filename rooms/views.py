from django.views.generic import DetailView
from django.shortcuts import render
from django.http import Http404
from . import models

# Create your views here.


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         print(room.amenities.all)
#         return render(request, "rooms/room_detail.html",{
#             'room': room,
#         })
#     except models.Room.DoesNotExist:
#         raise Http404()

class RoomDetail(DetailView):
    model = models.Room