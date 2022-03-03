from django.urls import path

from trackers.views import BMIPost, BMIFetch
app_name = 'trackers'

urlpatterns = [
    path('post_bmi/', BMIPost.as_view(), name='post-bmi'),
    path('fetch_bmi_data/', BMIFetch.as_view(), name='fetch-bmi'),
]