from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import authenticate

from account.models import User, Patient, Practitioner
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Telecom,Link

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

    # period = serializers.StringRelatedField(read_only=True)
    # contact_point = serializers.StringRelatedField(read_only=True)
    # deceased = serializers.StringRelatedField(read_only=True)
    # address = serializers.StringRelatedField(read_only=True)
    # human_name = serializers.StringRelatedField(read_only=True)
    # marital_status = serializers.StringRelatedField(read_only=True)
    # contact = serializers.StringRelatedField(read_only=True)
    # communication = serializers.StringRelatedField(read_only=True)
    # link = serializers.StringRelatedField(read_only=True)

    # token = serializers.CharField(max_length = 255, read_only=True)
    
    class Meta:
        model = Patient
        # fields = ('first_name','last_name', 'email', 'password','occupation',
        #           'period','contact_point','deceased','address','human_name',
        #           'marital_status','contact', 'communication','link','token')
        fields = '__all__'
    def create(self, validated_data):
        return Patient.objects.create_patient(**validated_data)

class PractitionerRegistrationSerializer(serializers.ModelSerializer):
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
        model = Practitioner
        fields = ('first_name','last_name', 'email', 'password', 'hospital_name','token')

    def create(self, validated_data):
        return Practitioner.objects.create_doctor(**validated_data)


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
                userObj = Practitioner.objects.get(email=user.email)
        except Practitioner.DoesNotExist:
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
        fields = ('start','end')

class ContactPointSerializer(serializers.ModelSerializer):
    
    period = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ContactPoint
        fields = ('system','value','use','rank','period')


class DeceasedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Deceased
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):

    period = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Address
        fields = ('use','address_type','text','line','city','district','state','postalCode','country','period')


class HumanNameSerializer(serializers.ModelSerializer):

    period = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = HumanName
        fields = ('use','text','family','given','prefix','suffix','period')


class MaritalStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MaritalStatus
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(read_only=True)
    telecom = serializers.StringRelatedField(read_only=True)
    address = serializers.StringRelatedField(read_only=True)
    period = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Contact
        fields = ('relationship','name','telecom','address','gender','period')

class CommunicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Communication
        fields = "__all__"


class TelecomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Telecom
        fields = ('system','value','use','rank','period')

class LinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Link
        fields = "__all__"

