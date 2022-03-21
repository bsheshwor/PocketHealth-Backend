from django.urls import path

from trackers.api.views import BmiVS, PressureVS, BloodSugarVS
app_name = 'trackers'

urlpatterns = [
    # path('post_bmi/', BMIPost.as_view(), name='post-bmi'),
    path('bmi/', BmiVS.as_view({'get': 'list', 'post':'create'}), name='list-bmi'),
    path('bmi/<int:pk>', BmiVS.as_view({'get': 'retrieve', 'put':'update', 'delete': 'destroy'}), name='retrieve-bmi'),

    path('pressure/', PressureVS.as_view({'get': 'list', 'post':'create'}), name='list-pressure'),
    path('pressure/<int:pk>', PressureVS.as_view({'get': 'retrieve', 'put':'update', 'delete': 'destroy'}), name='retrieve-pressure'),

    path('bloodsugar/', BloodSugarVS.as_view({'get': 'list', 'post':'create'}), name='list-bloodsugar'),
    path('bloodsugar/<int:pk>', BloodSugarVS.as_view({'get': 'retrieve', 'put':'update', 'delete': 'destroy'}), name='retrieve-bloodsugar'),
]