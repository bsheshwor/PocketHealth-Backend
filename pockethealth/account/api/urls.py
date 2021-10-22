from django.urls import path
from django.urls.resolvers import URLPattern

from .views import CustomerRegistration, DoctorRegistration, UserLogin

app_name = 'account'

urlpatterns = [
    path('customer_register/', CustomerRegistration.as_view(), name='customer_register'),
    path('doctor_register/', DoctorRegistration.as_view(), name='doctor_register'),
    path('login/', UserLogin.as_view(), name='login')
]