# main/urls.py

from .views import BookingView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', BookingView.as_view(), name='booking'),
]
    # Add other paths for different sections
# main/urls.py

