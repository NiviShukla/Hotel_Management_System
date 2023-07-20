from django.shortcuts import render, redirect

from django.views.generic import ListView, FormView
from .models import Room, Booking
from .forms import AvailabilityForm
from django.contrib import messages

from hotel.booking.availability import check_availability

import json

def main_view(request):
    return render(request, "main.html", {"name": "Hotel Management"})


class RoomList(ListView):
    model = Room
    
    
    
class BookingList(ListView):
    model = Booking
    
class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'
    
    
    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category = data['room_category'])
        available_list = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_list.append(room)
                
        if len(available_list) > 0:
            room = available_list[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out'],
        )
        
            booking.save()
            messages.success(self.request, "Booking created successfully.")
            return redirect('hotel:BookingView')
        
        else:
            messages.error(self.request, "This room category is booked. Please try another category.")
            return self.form_invalid(form)