from django.urls import path
from . import views

urlpatterns = [
    path('transporters', views.list_blood_transporters, name='list_blood_transporters'),
]