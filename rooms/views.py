from django.shortcuts import render

# Create your views here.


def room_detail(request):
    return render(request, "rooms/room_detail.html")