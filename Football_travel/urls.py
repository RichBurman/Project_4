from . import views
from django.urls import path


urlpatterns = [
    path('', views.TripList.as_view(), name='home'),
    path('mybookings.html', views.BookingList.as_view(), name='mybookings'),
]
