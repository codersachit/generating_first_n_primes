from django.urls import path

from . import views

urlpatterns = [
    path('input_n/', views.input_n_form, name='input_form'),
    path('input_request_id/', views.input_request_id_form, name='input_form'),
    path('input_n/generate_prime/', views.first_n_primes, name='first_n_primes'),
    path('input_request_id/get_prime/', views.get_first_n_primes, name='get_first_n_primes'),
]