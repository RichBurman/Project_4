from django.shortcuts import render
from django.views import generic
from .models import Trip, Booking

# Create your views here.


class TripList(generic.ListView):
    model = Trip
    template_name = 'index.html'


class BookingList(generic.ListView):
    template_name = 'mybookings.html'
    model = Booking

    def get_user_bookings(self, **kwargs):
        return get_user_bookings(Booking=self.request.user.booking_set.all(), **kwargs)
