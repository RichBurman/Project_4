from django.contrib import admin
from .models import Trip

# Register your models here.


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_id', 'trip_name', 'date', 'price', )
    search_fields = ('trip_name',)
