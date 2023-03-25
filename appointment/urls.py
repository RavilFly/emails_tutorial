from django.urls import path
from .views import AppointmentView


urlpatterns = [
    path('appointment/make/', AppointmentView.as_view(), name="appointments"),
]