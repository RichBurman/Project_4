from . import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('', views.TripList.as_view(), name='home'),
    path('mybookings',
         views.BookingList.as_view(), name='mybookings'),
    path('newbooking', views.newbooking, name='newbooking'),
    path('add', views.newbooking, name='addnewbooking'),
    path('edit/<int:booking_id>/', views.editbooking, name='editbooking'),
    path('delete/<booking_id>', views.deletebooking, name='deletebooking'),


]
