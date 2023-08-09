from django.contrib import admin
from .models import Trip, Booking

# Register your models here.


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_id', 'trip_name', 'date', 'price', )
    search_fields = ('trip_name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'trip_booked')
