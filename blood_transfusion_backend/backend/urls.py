from django.urls import path
from . import views

urlpatterns = [
    path('donor', views.donor_info, name='view_donor_info'),
    path('necessaryBloodProductsInCity', views.necessary_blood_products_in_city, name='view_necessary_blood_products_in_city'),
    path('newDonor', views.new_donor, name='view_new_donor'),

    path('', views.home_page, name='view_homeـpage'),
]