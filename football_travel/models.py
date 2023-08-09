from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date
from django.core.validators import MaxValueValidator

# Create your models here.


class Trip(models.Model):
    trip_name = models.CharField(max_length=50)
    trip_id = models.AutoField(primary_key=True)
    seats = models.IntegerField(default=80)
    remaining_seats = models.PositiveIntegerField(validators=[MaxValueValidator(80)])
    price=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return f"Name: {self.trip_name} ID Number: {self.trip_id}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=False, default=date.today)
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)
    trip_booked = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seats_required = models.IntegerField()
    total_cost = models.IntegerField(default=0)

    def __str__(self):
        return f"User: {self.user} booked {self.trip_booked} on {self.created_on}"
