from django import forms
from .models import Booking, Trip
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'trip_booked', 'seats_required', 'comment']
        labels = {
            'date':'Date of Booking',
            'trip_booked':'Selected Trip',
            'seats_required':'Number of Seats Required',
            'comment':'Additional Comments',
        }
