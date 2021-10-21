from typing_extensions import Required
from rest_framework import serializers
from django.conf import settings

from account import models

class UserProfileSerializer(serializers.ModelSerializer):
    "A serializer for our usr profile objects"

    class Meta:
        model = models.UserProfile
        fields = "__all__"
        extra_kwargs = {"password":{"write_only":True}}


class CustomerSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = models.Customer
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = models.Doctor
        fields = "__all__"

# class UserRegistrationSerializer(serializers.ModelSerializer):
    
#     class RegisterCustomerSerializer(serializers.ModelSerializer):
        
