from django import forms
from .models import Booking, Trip
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'comment', 'trip_booked', 'seats_required']
