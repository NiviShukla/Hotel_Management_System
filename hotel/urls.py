from django.urls import path
from .views import main_view, BookingView, BookingList, RoomList


app_name = 'hotel'

urlpatterns = [
    path("",main_view,name="main"),
    path('room_list/', RoomList.as_view(), name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name="BookingView"),
]
