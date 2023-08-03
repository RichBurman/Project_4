from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Trip, Booking
from .forms import BookingForm
from django.contrib.auth.models import User

# Create your views here.


class TripList(generic.ListView):
    model = Trip
    template_name = 'index.html'


class BookingList(generic.ListView):
    template_name = 'mybookings.html'
    model = Booking

    def get_user_bookings(self):
        context = super().get_user_bookings()
        context['Booking'] = self.request.user.booking_set.all()
        return context


def newbooking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('mybookings')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'newbooking.html', context)


def editbooking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('mybookings')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'editbooking.html', context)
