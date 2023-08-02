from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Trip(models.Model):
    trip_name = models.CharField(max_length=50)
    trip_id = models.AutoField(primary_key=True)
    seats = models.DecimalField(decimal_places=0, max_digits=2)
    remaining_seats = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()

    def __str__(self):
        return f"Name: {self.trip_name} ID Number: {self.trip_id}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_booking = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seats_required = models.DecimalField(decimal_places=0, max_digits=2)
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.trip_booking}. Booked by {self.user} needing {self.seats_required} seats'
