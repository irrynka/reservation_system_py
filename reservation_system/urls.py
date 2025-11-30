from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/book/', views.booking_list, name='booking_list'),
    path('booking/success/', views.booking_success, name='booking_success'),
]
