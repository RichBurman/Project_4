from . import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('', views.TripList.as_view(), name='home'),
    path('mybookings.html', views.BookingList.as_view(), name='mybookings'),
    path('newbooking.html', views.newbooking, name='newbooking'),
]
