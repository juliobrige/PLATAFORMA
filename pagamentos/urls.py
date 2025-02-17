# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('mpesa/pagar/', views.lipa_na_mpesa_online, name='mpesa_pagar'),
    path('mpesa/callback/', views.mpesa_callback, name='mpesa_callback'),

]