from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import authenticate

from account.models import User, Patient, Practitioner
from account import patientModels

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
        model = patientModels.Period
        fields = "__all__"

class ContactPointSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patientModels.ContactPoint
        fields = '__all__'


class DeceasedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patientModels.Deceased
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patientModels.Address
        fields = "__all__"


class HumanNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patientModels.HumanName
        fields = "__all__"


class MaritalStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patientModels.MaritalStatus
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patientModels.Contact
        fields = "__all__"

class CommunicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patientModels.Communication
        fields = "__all__"

class LinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patientModels.Link
        fields = "__all__"



# class PractitionerPeriodSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = practitionerModels.Period
#         fields = "__all__"

# class PractitionerContactPointSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = practitionerModels.ContactPoint
#         fields = '__all__'


# class PractitionerDeceasedSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = practitionerModels.Deceased
#         fields = "__all__"


# class PractitionerAddressSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = practitionerModels.Address
#         fields = "__all__"


# class PractitionerHumanNameSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = practitionerModels.HumanName
#         fields = "__all__"


# class PractitionerMaritalStatusSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = practitionerModels.MaritalStatus
#         fields = "__all__"


# class PractitionerContactSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = practitionerModels.Contact
#         fields = "__all__"

# class PractitionerCommunicationSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = practitionerModels.Communication
#         fields = "__all__"

# class PractitionerSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = practitionerModels.Link
#         fields = "__all__"