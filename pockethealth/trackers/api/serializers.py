
from rest_framework import serializers
from trackers.models import BMIData
class BMISerializer(serializers.ModelSerializer):
    class Meta:
        model = BMIData
        fields = ['user', 'weight_in_kg', 'height_in_cm']

