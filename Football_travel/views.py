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
    # Check if the form has been submitted via POST
    if request.method == "POST":
        # Create a form instance and populate it with the submitted data
        form = BookingForm(request.POST)

        # Check if the form data is valid
        if form.is_valid():
            # Associate the booking with the current logged-in user
            form.instance.user = request.user

            # Save the booking instance to the database
            booking = form.save()

            # Get the corresponding Trip object for the booking
            trip = booking.trip_booked

            # Update the remaining seats for the trip after booking
            trip.remaining_seats -= booking.seats_required
            trip.save()

            # Show a success message to the user
            messages.success(request, "Booking has been successfully made!")

            # Redirect the user to their bookings page after successful booking
            return redirect('mybookings')
    else:
        # If the request is not a POST, create an empty form instance
        form = BookingForm()

    # Prepare the context to render the template with the form
    context = {
        'form': form,
    }

    # Render the template 'newbooking.html' with the form context
    return render(request, 'newbooking.html', context)


@login_required
def editbooking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
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
    booking.delete()
    messages.success(request, "Booking has been deleted!")
    return redirect('mybookings')
