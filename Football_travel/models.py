from django.db import models

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
    name = models.CharField(max_length=50)
    email = models.EmailField()
    userid = models.DecimalField(decimal_places=0, max_digits=3)
    trip_id = models.DecimalField(decimal_places=0, max_digits=3)
    trip_name = models.CharField(max_length=50)
    seats = models.DecimalField(decimal_places=0, max_digits=2)
    remaining_seats =models.DecimalField(decimal_places=2, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()

    def __str__(self):
        return f"Name: {self.trip_name} ID Number: {self.trip_id} Email: {self.email}"
