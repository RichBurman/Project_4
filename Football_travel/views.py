from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Trip, Booking
from .forms import BookingForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


@login_required
def newbooking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            booking = form.save()
            trip = booking.trip_booked
            trip.remaining_seats -= booking.seats_required
            trip.save()
            messages.success(request, "Booking has been successfully made!")
            return redirect('mybookings')
    else:
        form = BookingForm()

    context = {
        'form': form,
    }

    return render(request, 'newbooking.html', context)


@login_required
def editbooking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        # Store the original number of seats required
        original_seats_required = booking.seats_required
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.instance.user = request.user
            booking = form.save()
            # Update the remaining seats of the trip based on the change in seats required
            trip = booking.trip_booked
            trip.remaining_seats += original_seats_required - booking.seats_required
            trip.save()

            messages.success(request, "Booking has been edited successfully!")
            return redirect('mybookings')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'editbooking.html', context)


@login_required
def deletebooking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    trip = booking.trip_booked
    # add the seats back to the trip
    trip.remaining_seats += booking.seats_required
    trip.save()
    booking.delete()
    messages.success(request, "Booking has been deleted!")
    return redirect('mybookings')
