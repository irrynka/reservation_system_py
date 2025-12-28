from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Room, Booking
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

@login_required
def booking_list(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        Booking.objects.create(
            user=request.user,
            room=room,
            start_date=start_date,
            end_date=end_date,
            is_confirmed=True
        )
        return redirect('booking_success')

    return render(request, 'book_list.html', {'room': room})


def booking_success(request):
    return render(request, 'booking_success.html')



def auth_view(request):
    if request.user.is_authenticated:
        return redirect('room_list')

    login_form = AuthenticationForm()
    register_form = UserCreationForm()
    active_tab = 'login'

    if request.method == 'POST':
        if 'login_submit' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('room_list')
            else:
                active_tab = 'login'

        elif 'register_submit' in request.POST:
            register_form = UserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('room_list')
            else:
                active_tab = 'register'

    return render(request, 'auth.html', {
        'login_form': login_form,
        'register_form': register_form,
        'active_tab': active_tab
    })

@login_required
def user_logout(request):
    logout(request)
    return redirect('auth') 