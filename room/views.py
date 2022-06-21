from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Room, Message
# Create your views here.

#ensure user is authenticated before access
@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms':rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]


    return render(request, 'room/room.html', {'room': room, 'messages':messages}) 