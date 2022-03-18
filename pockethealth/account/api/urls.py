from django.urls import path
from django.urls.resolvers import URLPattern

from .views import CustomerRegistration, DoctorRegistration, UserLogin,PeriodViewSet,ContactPointViewSet,DeceasedViewSet,AddressViewSet,HumanNameViewSet,MaritalStatusViewSet,ContactViewSet,CommunicationViewSet,LinkViewSet

app_name = 'account'

urlpatterns = [
    path('customer_register/', CustomerRegistration.as_view(), name='customer_register'),
    path('doctor_register/', DoctorRegistration.as_view(), name='doctor_register'),
    path('login/', UserLogin.as_view(), name='login'),
    # path('period/', PeriodViewSet.as_view(), name='period'),
    # path('contact_point/', ContactPointViewSet.as_view(), name='contact_point'),
    # path('deceased/', DeceasedViewSet.as_view(), name='deceased'),
    # path('address/', AddressViewSet.as_view(), name='address'),
    # path('human_name/', HumanNameViewSet.as_view(), name='human_name'),
    # path('marital_status/', MaritalStatusViewSet.as_view(), name='marital_status'),
    # path('contact/', ContactViewSet.as_view(), name='contact'),
    # path('communication/', CommunicationViewSet.as_view(), name='communication'),
    # path('link/', LinkViewSet.as_view(), name='link')
]