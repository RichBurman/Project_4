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
            booking = form.save(commit=False)

            trip = booking.trip_booked
            remaining_seats = trip.remaining_seats

            if booking.seats_required > remaining_seats:
                messages.error(
                    request, f"Sorry, there are only {remaining_seats} seats available. You are unable to book {booking.seats_required} seats.")
            else:
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
    trip = booking.trip_booked
    trip.remaining_seats += booking.seats_required
    trip.save()
    booking.delete()
    messages.success(request, "Booking has been deleted!")
    return redirect('mybookings')

    from django.shortcuts import render


def booking_success(request, booking_id):
    booking = Booking.objects.get(id=booking_id)

    context = {

        'booking': booking


    }

    return render(request, 'booking_success.html', context)
