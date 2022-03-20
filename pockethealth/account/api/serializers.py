from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import authenticate

from account.models import User, Customer, Doctor,Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Link

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 150,
        min_length = 8,
        write_only = True
    )

    # password_confirm = serializers.CharField(
    #     max_length = 150,
    #     min_length = 8,
    #     write_only = True
    # )

    token = serializers.CharField(max_length = 255, read_only=True)
    
    class Meta:
        model = Customer
        fields = ('first_name','last_name', 'email', 'password','occupation', 'token')

    def create(self, validated_data):
        return Customer.objects.create_customer(**validated_data)

class DoctorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 150,
        min_length = 8,
        write_only = True
    )

    # password_confirm = serializers.CharField(
    #     max_length = 150,
    #     min_length = 8,
    #     write_only = True
    # )

    token = serializers.CharField(max_length = 255, read_only=True)

    class Meta:
        model = Doctor
        fields = ('first_name','last_name', 'email', 'password', 'hospital_name','token')

    def create(self, validated_data):
        return Doctor.objects.create_doctor(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length = 255)
    password = serializers.CharField(max_length=150, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self,data):
        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            userObj = Customer.objects.get(email=user.email)
        except Customer.DoesNotExist:
            userObj = None
        
        try:
            if userObj is None:
                userObj = Doctor.objects.get(email=user.email)
        except Doctor.DoesNotExist:
            raise serializers.ValidationError(
                'User not given email and password does not exist'
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
 
        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
    
        return {
            'email': user.email,
            'token': user.token
        }

class PeriodSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Period
        fields = "__all__"

class ContactPointSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = ContactPoint
        fields = '__all__'


class DeceasedSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Deceased
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Address
        fields = "__all__"


class HumanNameSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = HumanName
        fields = "__all__"


class MaritalStatusSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = MaritalStatus
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Contact
        fields = "__all__"

class CommunicationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Communication
        fields = "__all__"

class LinkSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Link
        fields = "__all__"