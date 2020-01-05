from django.shortcuts import render
from django.views.generic import ListView
from datetime import datetime
from rooms import models as room_models
# Create your views here.


def all_rooms(request):
    rooms = room_models.Room.objects.all()
    return render(request, "core/room_list.html", context={
        "rooms": rooms
    })

class HomeView(ListView):
    model = room_models.Room
    template_name = "core/room_list.html"
    paginate_by = 10
    paginate_orphans = 5
    page_kwarg = "page"
    ordering = "created_at"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.now()
        return context

