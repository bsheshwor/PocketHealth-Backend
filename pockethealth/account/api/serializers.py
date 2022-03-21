from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import authenticate

from account.models import User, Patient, Doctor
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Link

class PatientRegistrationSerializer(serializers.ModelSerializer):
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

    period = serializers.StringRelatedField(read_only=True)
    contact_point = serializers.StringRelatedField(read_only=True)
    deceased = serializers.StringRelatedField(read_only=True)
    address = serializers.StringRelatedField(read_only=True)
    human_name = serializers.StringRelatedField(read_only=True)
    marital_status = serializers.StringRelatedField(read_only=True)
    contact = serializers.StringRelatedField(read_only=True)
    communication = serializers.StringRelatedField(read_only=True)
    link = serializers.StringRelatedField(read_only=True)

    token = serializers.CharField(max_length = 255, read_only=True)
    
    class Meta:
        model = Patient
        fields = ('first_name','last_name', 'email', 'password','occupation',
                  'period','contact_point','deceased','address','human_name',
                  'marital_status','contact', 'communication','link','token')

    def create(self, validated_data):
        return Patient.objects.create_patient(**validated_data)

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
            userObj = Patient.objects.get(email=user.email)
        except Patient.DoesNotExist:
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

    class Meta:
        model = Period
        fields = "__all__"

class ContactPointSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactPoint
        fields = '__all__'


class DeceasedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Deceased
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = "__all__"


class HumanNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HumanName
        fields = "__all__"


class MaritalStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MaritalStatus
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = "__all__"

class CommunicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Communication
        fields = "__all__"

class LinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Link
        fields = "__all__"