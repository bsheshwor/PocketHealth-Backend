from django.urls import path
from django.urls.resolvers import URLPattern

from .views import PatientRegistration, DoctorRegistration, UserLogin,PeriodViewSet,ContactPointViewSet,DeceasedViewSet,AddressViewSet,HumanNameViewSet,MaritalStatusViewSet,ContactViewSet,CommunicationViewSet,LinkViewSet

app_name = 'account'

urlpatterns = [
    path('customer_register/', PatientRegistration.as_view(), name='customer_register'),
    path('doctor_register/', DoctorRegistration.as_view(), name='doctor_register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('period/', PeriodViewSet.as_view({'get': 'list', 'post':'create'}), name="create_period"),
    path('period/<int:pk>', PeriodViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='period'),
    path('contact_point/', ContactPointViewSet.as_view({'get': 'list', 'post':'create'}), name='contact_point'),
    path('contact_point/<int:pk>', ContactPointViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='contact-point'),
    path('deceased/', DeceasedViewSet.as_view({'get': 'list', 'post':'create'}), name='deceased'),
    path('deceased/<int:pk>', DeceasedViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='deceased-detail'),
    path('address/', AddressViewSet.as_view({'get': 'list', 'post':'create'}), name='address'),
    path('address/<int:pk>', AddressViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='address-detail'),
    path('human_name/', HumanNameViewSet.as_view({'get': 'list', 'post':'create'}), name='human_name'),
    path('human_name/<int:pk>', HumanNameViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='human_name-detail'),
    path('marital_status/', MaritalStatusViewSet.as_view({'get': 'list', 'post':'create'}), name='marital_status'),
    path('marital_status/<int:pk>', MaritalStatusViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='marital_status-detail'),
    path('contact/', ContactViewSet.as_view({'get': 'list', 'post':'create'}), name='contact'),
    path('contact/<int:pk>', ContactViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='contact-detail'),
    path('communication/', CommunicationViewSet.as_view({'get': 'list', 'post':'create'}), name='communication'),
    path('communication/<int:pk>', CommunicationViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='communication-detail'),
    path('link/', LinkViewSet.as_view({'get': 'list', 'post':'create'}), name='link'),
    path('link/<int:pk>', LinkViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'
                                        }), name='link-detail'),
]