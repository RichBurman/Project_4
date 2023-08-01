from django.shortcuts import render
from django.views import generic
from .models import Trip

# Create your views here.


class TripList(generic.ListView):
    model = Trip
    template_name = 'index.html'
