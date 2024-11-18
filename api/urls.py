from django.urls import path
from .views import RoomBookingView

urlpatterns = [
    path('api/roombooking/', RoomBookingView.as_view(), name='room-booking'),
]
