from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import authenticate

from account.models import User, Patient, Practitioner
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Telecom,Link
from account.organization import Organization, OrganizationContact
from account.healthcareService import HealthcareService, HealthcareCategory, Type, Speciality, ServiceProvisionCode, Program,ReferralMethod, availableTime, notAvailableTime
from account.careteam import CareTeam, StatusCode, ParticipantRole, Participant, ReasonCode, Annotation, Author
from account.location import  Location, Status, OperationalStatus, Mode, Types, PhysicalLocationType, Position, HoursOfOperation

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

class OrganizationSerializer(serializers.ModelSerializer):
    telecom = serializers.StringRelatedField(read_only=True)
    address = serializers.StringRelatedField(read_only=True)
    contact = serializers.StringRelatedField(read_only=True)
 
    class Meta:
        model = Organization
        fields = ("active","types","name","alias", "telecom","address","contact")


class OrganizationContactSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(read_only=True)
    telecom = serializers.StringRelatedField(read_only=True)
    address = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OrganizationContact
        fields = ("purpose","name","telecom","address")

class HealthcareServiceSerializer(serializers.ModelSerializer):
    providedBy = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    types = serializers.StringRelatedField(read_only=True)
    speciality = serializers.StringRelatedField(read_only=True)
    location = serializers.StringRelatedField(read_only=True)
    telecom = serializers.StringRelatedField(read_only=True)
    serviceProvisionCode = serializers.StringRelatedField(read_only=True)
    program = serializers.StringRelatedField(read_only=True)
    communication = serializers.StringRelatedField(read_only=True)
    referralMethod = serializers.StringRelatedField(read_only=True)
    availableTime = serializers.StringRelatedField(read_only=True)
    notAvailable = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = HealthcareService
        fields = ("active","providedBy","category","types","speciality","location","name","comment","serviceProvisionCode","program","communication","referralMethod","appointmentRequired","availableTime","notAvailable","availabilityExceptions",)

class HealthcareCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthcareCategory
        fields = ("text",)

class TypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Type
        fields = ("text",)

class SpecialitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Speciality
        fields = ("text",)
    
class ServiceProvisionCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceProvisionCode
        fields =("text",)


class ProgramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Program
        fields = ("text",)

class ReferralMethodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReferralMethod
        fields = ("text",)

class availableTimeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = availableTime
        fields = ("daysOfWeek","allDay","availableStartTime","availabelEndTime",)
    
class notAvailableTimeSerializer(serializers.ModelSerializer):
    during = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = notAvailableTime
        fields = ("description","during")


class CareTeamSerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField(read_only=True)
    period = serializers.StringRelatedField(read_only=True)
    reasonCode = serializers.StringRelatedField(read_only=True)
    managingOrganization = serializers.StringRelatedField(read_only=True)
    telecom = serializers.StringRelatedField(read_only=True)
    note = serializers.StringRelatedField(read_only=True)
   
    class Meta:
        model = CareTeam
        fields = ("status","name","period","reasonCode","managingOrganization","telecom","note",)
    
class StatusCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StatusCode
        fields = ("text",)

class ParticipantRoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParticipantRole
        fields = ("text")
    
# class ParticipantSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Participant
#         fields = ("text")


class ReasonCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReasonCode
        fields = ("text")

class AnnotationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Annotation
        fields = ("time","text")

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ("authorString",)


class LocationSerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField(read_only=True)
    operationalStatus = serializers.StringRelatedField(read_only=True)
    mode = serializers.StringRelatedField(read_only=True)
    types = serializers.StringRelatedField(read_only=True)
    telecom = serializers.StringRelatedField(read_only=True)
    address = serializers.StringRelatedField(read_only=True)
    physicalType = serializers.StringRelatedField(read_only=True)
    position = serializers.StringRelatedField(read_only=True)
    managinOrganization = serializers.StringRelatedField(read_only=True)
    hourseOfOperation = serializers.StringRelatedField(read_only=True)
    telecom = serializers.StringRelatedField(read_only=True)
    address = serializers.StringRelatedField(read_only=True)
   
    class Meta:
        model = Location
        fields = ("status","operationalStatus","name","alias","description","mode","types","telecom","address","physicalType","position","managingOrganization","hoursOfOperation","availabilityExceptions")

class StatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Status
        fields = ("text",)

class OperationalStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OperationalStatus
        fields = ("text",)

class ModeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mode
        fields = ("text",)

class TypesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Types
        fields = ("text",)

class PhysicalLocationTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PhysicalLocationType
        fields = ("text",)

class PositionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Position
        fields = ("longitude","latitude","altitude")

class HoursOfOperationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HoursOfOperation
        fields = ("daysOfWeek","allDay","openingTime","closingTime")
