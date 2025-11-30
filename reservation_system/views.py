from django.shortcuts import render, redirect
from .models import Room, Booking
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def home(request):
    return HttpResponse("Вітаю! Це головна сторінка системи бронювання.")



def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

@login_required 
def booking_list(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        booking = Booking(
            user=request.user,
            room=room,
            start_date=start_date,
            end_date=end_date,
            is_confirmed=True
        )
        booking.save()
        return redirect('booking_success')

    return render(request, 'book_list.html', {'room': room})

def booking_success(request):
    return render(request, 'booking_success.html')
