from django import forms
from .models import Booking, Trip
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['trip_booked'].queryset = Trip.objects.all()
        self.fields['trip_booked'].label_from_instance = lambda obj: obj.trip_name

    class Meta:
        model = Booking
        fields = ['date', 'trip_booked',
                  'seats_required', 'comment']
        labels = {
            'date': 'Date of Booking',
            'trip_booked': 'Selected Trip',
            'seats_required': 'Number of Seats Required',
            'comment': 'Additional Comments',
        }
