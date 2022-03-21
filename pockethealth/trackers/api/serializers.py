
from rest_framework import serializers
from trackers.models import BMIData, PressureData, BloodSugarData
class BMISerializer(serializers.ModelSerializer):
    class Meta:
        model = BMIData
        fields = ['user', 'weight_in_kg', 'height_in_cm']

class PressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressureData
        fields = ['user', 'value']

class BloodSugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodSugarData
        fields = ['user', 'value']

