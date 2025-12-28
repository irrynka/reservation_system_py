from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('booking/<int:room_id>/', views.booking_list, name='booking_list'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('auth/', views.auth_view, name='auth'),
    path('logout/', views.user_logout, name='user_logout'),
]
