from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import authenticate
from drf_writable_nested.serializers import WritableNestedModelSerializer

from account.models import User, Patient, Practitioner, PatientRegisterModel, PractitionerRegisterModel
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Telecom,Link, Qualification,QualificationCodeableConcept
from account.organization import Organization, OrganizationContact
from account.healthcareService import HealthcareService, HealthcareCategory, Type, Speciality, ServiceProvisionCode, Program,ReferralMethod, availableTime, notAvailableTime
from account.careteam import CareTeam, StatusCode, ParticipantRole, Participant, ReasonCode, Annotation,Note, Author
from account.location import  Location, Status, OperationalStatus, Mode, Types, PhysicalLocationType, Position, HoursOfOperation

class PeriodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Period
        fields = ('pk','start','end')

class ContactPointSerializer(WritableNestedModelSerializer):
    
    # period = serializers.StringRelatedField(read_only=True)
    period = PeriodSerializer(many=True,required=False)

    class Meta:
        model = ContactPoint
        fields = ('pk','system','value','use','rank','period')
    
    # def create(self, validated_data):
    #     periods = validated_data.pop("period")
    #     contactpoint_instance = ContactPoint.objects.create(**validated_data)
    #     if periods:
    #         for per in periods:
    #             Period.objects.create(contactpoint=contactpoint_instance,**per)
    #     return contactpoint_instance

    # def update(self, instance, validated_data):
    #     if validated_data.get('period'):
    #         period_data = validated_data.get('period')
    #         period_serializer = PeriodSerializer(data=period_data)

    #         if period_serializer.is_valid():
    #             period = period_serializer.update(instance=instance.period,
    #                                                 validated_data=period_serializer.validated_data)
    #             validated_data['period'] = period

    #     return super().update(instance, validated_data)

class DeceasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deceased
        fields = "__all__"


class AddressSerializer(WritableNestedModelSerializer):

    # period = serializers.StringRelatedField(read_only=True)
    period = PeriodSerializer(many=True,required=False)

    class Meta:
        model = Address
        fields = ('pk','use','address_type','text','line','city','district','state','postalCode','country','period')


class TelecomSerializer(WritableNestedModelSerializer):
    contactpoint = ContactPointSerializer(many=True,required=False)
    class Meta:
        model = Telecom
        fields = ('pk','contactpoint')

class HumanNameSerializer(WritableNestedModelSerializer):
    period = PeriodSerializer(many=True,required=False)

    # period = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = HumanName
        fields = ('pk','use','text','family','given','prefix','suffix','period')


class MaritalStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MaritalStatus
        fields = ("pk","text")



class ContactSerializer(WritableNestedModelSerializer):
    # name = serializers.StringRelatedField(read_only=True)
    # telecom = serializers.StringRelatedField(read_only=True)
    # address = serializers.StringRelatedField(read_only=True)
    # period = serializers.StringRelatedField(read_only=True)
    
    name = HumanNameSerializer(many=True,required=False)
    telecom = TelecomSerializer(many=True,required=False)
    address = AddressSerializer(many=True,required=False)
    period = PeriodSerializer( many=True,required=False)


    class Meta:
        model = Contact
        fields = ('pk','relationship','name','telecom','address','gender','period')

class CommunicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Communication
        fields = ("pk","language","preferred")


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ("pk","link_type")

class OrganizationContactSerializer(WritableNestedModelSerializer):
    # name = serializers.StringRelatedField(read_only=True)
    # telecom = serializers.StringRelatedField(read_only=True)
    # address = serializers.StringRelatedField(read_only=True)
    name = HumanNameSerializer(many=True,required=False)   
    telecom = TelecomSerializer(many=True,required=False)
    address = AddressSerializer(many=True,required=False)
    
    class Meta:
        model = OrganizationContact
        fields = ("pk","purpose","name","telecom","address")


class OrganizationSerializer(WritableNestedModelSerializer):
    # telecom = serializers.StringRelatedField(read_only=True)
    # address = serializers.StringRelatedField(read_only=True)
    # contact = serializers.StringRelatedField(read_only=True)
    telecom = TelecomSerializer(many=True,required=False)
    address = AddressSerializer(many=True,required=False)
    contact = OrganizationContactSerializer(many=True,required=False)

    class Meta:
        model = Organization
        fields = ("pk","active","types","name","alias", "telecom","address","contact")


class HealthcareCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthcareCategory
        fields = ("pk","text",)

class TypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Type
        fields = ("pk","text",)

class SpecialitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Speciality
        fields = ("pk","text",)
    
class ServiceProvisionCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceProvisionCode
        fields =("pk","text",)


class ProgramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Program
        fields = ("pk","text",)

class ReferralMethodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReferralMethod
        fields = ("pk","text",)

class availableTimeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = availableTime
        fields = ("pk","daysOfWeek","allDay","availableStartTime","availabelEndTime",)
    
class notAvailableTimeSerializer(WritableNestedModelSerializer):
    during = serializers.StringRelatedField(many=True,required=False)

    class Meta:
        model = notAvailableTime
        fields = ("pk","description","during")

class QualificationCodeableConceptSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QualificationCodeableConcept
        fields = ("pk","text",)

class QualificationSerializer(serializers.ModelSerializer):
    period = PeriodSerializer(many=True,required=False)
    code = QualificationCodeableConceptSerializer(many=True,required=False)
    
    class Meta:
        model = Qualification
        fields = ("pk","code","text")


class HealthcareServiceSerializer(WritableNestedModelSerializer):
    # providedBy = serializers.StringRelatedField(read_only=True)
    # # category = serializers.StringRelatedField(read_only=True)
    # # types = serializers.StringRelatedField(read_only=True)
    # speciality = serializers.StringRelatedField(read_only=True)
    # location = serializers.StringRelatedField(read_only=True)
    # telecom = serializers.StringRelatedField(read_only=True)
    # serviceProvisionCode = serializers.StringRelatedField(read_only=True)
    # program = serializers.StringRelatedField(read_only=True)
    # communication = serializers.StringRelatedField(read_only=True)
    # referralMethod = serializers.StringRelatedField(read_only=True)
    # availableTime = serializers.StringRelatedField(read_only=True)
    # notAvailable = serializers.StringRelatedField(read_only=True)
    
    category = HealthcareCategorySerializer(many=True,required=False)
    types = TypeSerializer(many=True,required=False)
    speciality = SpecialitySerializer(many=True,required=False)
#    - location = TypeSerializer(many=True, read_only=True)
    telecom = TelecomSerializer(many=True,required=False)
    serviceProvisionCode = ServiceProvisionCodeSerializer( many=True,required=False)
    program = ProgramSerializer(many=True,required=False)
    communication = CommunicationSerializer(many=True,required=False)
    referralMethod = ReferralMethodSerializer(many=True,required=False)
    availableTime = availableTimeSerializer(many=True,required=False)
    notAvailable = notAvailableTimeSerializer(many=True,required=False)
 

    class Meta:
        model = HealthcareService
        fields = ("pk","active","providedBy","category","types","speciality","telecom","location","name","comment","serviceProvisionCode","program","communication","referralMethod","appointmentRequired","availableTime","notAvailable","availabilityExceptions",)

    
class StatusCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StatusCode
        fields = ("pk","text",)


class ParticipantRoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParticipantRole
        fields = ("pk","text")
    
# class ParticipantSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Participant
#         fields = ("text")

class ParticipantSerializer(WritableNestedModelSerializer):
    
    role = ParticipantRoleSerializer(many=True,required=False)
    onBehalfOf = OrganizationSerializer(many=True,required=False)
    period = PeriodSerializer(many=True,required=False)

    class Meta:
        model = Participant
        fields = ("pk","role","onBehalfOf","period")


class ReasonCodeSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = ReasonCode
        fields = ("pk","text")


class AnnotationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Annotation
        fields = ("pk","time","text")

class NoteSerializer(WritableNestedModelSerializer):
    
    annotation = AnnotationSerializer(many=True,required=False)

    class Meta:
        model = Note
        fields = ("pk","annotation")

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ("pk","authorString",)

class CareTeamSerializer(WritableNestedModelSerializer):
    # status = serializers.StringRelatedField(read_only=True)
    # period = serializers.StringRelatedField(read_only=True)
    # reasonCode = serializers.StringRelatedField(read_only=True)
    # managingOrganization = serializers.StringRelatedField(read_only=True)
    # telecom = serializers.StringRelatedField(read_only=True)
    # note = serializers.StringRelatedField(read_only=True)

    status = StatusCodeSerializer(many=True,required=False)
    period = PeriodSerializer(many=True,required=False)
    participant = ParticipantSerializer(many=True,required=False)
    managingOrganization = OrganizationSerializer(many=True,required=False)
    telecom = TelecomSerializer(many=True,required=False)
    note = NoteSerializer(many=True,required=False)
    reasonCode = ReasonCodeSerializer(many=True,required=False)

    class Meta:
        model = CareTeam
        fields = ("pk","status","name","period","participant","reasonCode","managingOrganization","telecom","note",)


class StatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Status
        fields = ("pk","text",)

class OperationalStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OperationalStatus
        fields = ("pk","text",)

class ModeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mode
        fields = ("pk","text",)

class TypesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Types
        fields = ("pk","text",)

class PhysicalLocationTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PhysicalLocationType
        fields = ("pk","text",)

class PositionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Position
        fields = ("pk","longitude","latitude","altitude")

class HoursOfOperationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HoursOfOperation
        fields = ("pk","daysOfWeek","allDay","openingTime","closingTime")


class LocationSerializer(WritableNestedModelSerializer):
    # status = serializers.StringRelatedField(read_only=True)
    # operationalStatus = serializers.StringRelatedField(read_only=True)
    # mode = serializers.StringRelatedField(read_only=True)
    # types = serializers.StringRelatedField(read_only=True)
    # telecom = serializers.StringRelatedField(read_only=True)
    # address = serializers.StringRelatedField(read_only=True)
    # physicalType = serializers.StringRelatedField(read_only=True)
    # position = serializers.StringRelatedField(read_only=True)
    # managinOrganization = serializers.StringRelatedField(read_only=True)
    # hourseOfOperation = serializers.StringRelatedField(read_only=True)
    # telecom = serializers.StringRelatedField(read_only=True)
    # address = serializers.StringRelatedField(read_only=True)
   
    status = StatusCodeSerializer(many=True,required=False)
    operationalStatus = OperationalStatusSerializer(many=True,required=False)
    mode = ModeSerializer(many=True, required=False)
    types = TypesSerializer(many=True, required=False)
    telecom = TelecomSerializer(many=True, required=False)
    address = AddressSerializer(many=True, required=False)
    physicalType = PhysicalLocationTypeSerializer(many=True, required=False)
    position = PositionSerializer(many=True, required=False)
    managingOrganization = OrganizationSerializer(many=True, required=False)
    hoursOfOperation = HoursOfOperationSerializer(many=True, required=False)


    class Meta:
        model = Location
        fields = ("pk","status","operationalStatus","name","alias","description","mode","types","telecom","address","physicalType","position","managingOrganization","hoursOfOperation","availabilityExceptions")


class PatientRegisterModelSerializer(WritableNestedModelSerializer):
    name = HumanNameSerializer(many=True,required=False)
    telecom = TelecomSerializer(many=True, required=False)
    address = AddressSerializer(many=True, required=False)
    maritalStatus = MaritalStatusSerializer(many=True, required=False)
    # photo
    contact = ContactSerializer(many=True, required=False)
    communication = CommunicationSerializer(many=True, required=False)
    managingOrganization = OrganizationSerializer(many=True, required=False)
    link = LinkSerializer(many=True, required=False)

    class Meta:
        model = PatientRegisterModel
        fields = ("pk","active","name","telecom","gender","birthDate","address","maritalStatus","contact","communication","managingOrganization","link")


class PractitionerRegisterModelSerializer(WritableNestedModelSerializer):
    name = HumanNameSerializer(many=True,required=False)
    telecom = TelecomSerializer(many=True, required=False)
    address = AddressSerializer(many=True, required=False)
    # photo
    qualification = QualificationSerializer(many=True, required=False)
    communication = CommunicationSerializer(many=True, required=False)
    class Meta:
        model = PractitionerRegisterModel
        fields = ("pk","active","name","telecom","address","gender","birthDate","qualification","communication")


class PatientRegistrationSerializer(serializers.ModelSerializer):
    # patient = PatientRegisterModelSerializer(required=False)
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

    token = serializers.CharField(max_length = 255, read_only=True)
    
    class Meta:
        model = Patient
        # fields = ('first_name','last_name', 'email', 'password','occupation',
        #           'period','contact_point','deceased','address','human_name',
        #           'marital_status','contact', 'communication','link','token'"patient")
        fields = ("pk","email","password","token",)

    def create(self, validated_data):
        return Patient.objects.create_patient(**validated_data)

class PractitionerRegistrationSerializer(serializers.ModelSerializer):
    # practitioner = PractitionerRegisterModelSerializer(required=False)
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
        # fields = ('first_name','last_name', 'email', 'password', 'hospital_name','token'"practitioner")
        fields = ("pk","email","password","token",)

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
