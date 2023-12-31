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
    content_object_name = 'trips'


class BookingList(generic.ListView):
    model = Booking
    template_name = 'mybookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bookings = context['bookings']
        for booking in bookings:
            booking.total_cost = booking.trip_booked.price * booking.seats_required
        return context


@login_required
def newbooking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            booking = form.save(commit=False)

            trip = booking.trip_booked
            remaining_seats = trip.remaining_seats
            total_cost = trip.price * booking.seats_required

            if booking.seats_required > remaining_seats:
                messages.error(
                    request, f"Sorry, there are only {remaining_seats} seats available. You are unable to book {booking.seats_required} seats.")
            else:
                booking.total_cost = total_cost
                booking.save()

                trip.remaining_seats -= booking.seats_required
                trip.save()

                messages.success(
                    request, "Booking has been successfully made!")
                return redirect('booking_success', booking_id=booking.id)
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
        original_seats_required = booking.seats_required
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.instance.user = request.user
            updated_booking = form.save(commit=False)
            trip = booking.trip_booked
            remaining_seats = trip.remaining_seats

            if updated_booking.seats_required > remaining_seats + original_seats_required:
                messages.error(
                    request, f"Sorry, there are only {remaining_seats} seats available. You are unable to book  {updated_booking.seats_required} seats.")
            else:
                updated_booking.total_cost = trip.price * updated_booking.seats_required
                updated_booking.save()
                trip.remaining_seats += original_seats_required - updated_booking.seats_required
                trip.save()

                messages.success(
                    request, "Booking has been edited successfully!")
                return redirect('mybookings')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'editbooking.html', context)


@login_required
def deletebooking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.user != request.user:
        messages.error(
            request, "You are not authorized to delete this booking.")
        return redirect('mybookings')

    trip = booking.trip_booked
    trip.remaining_seats += booking.seats_required
    trip.save()
    booking.delete()
    messages.success(request, "Booking has been deleted!")
    return redirect('mybookings')


def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    total_cost = booking.trip_booked.price * booking.seats_required
    context = {
        'booking': booking,
        'total_cost': total_cost
    }
    return render(request, 'booking_success.html', context)
