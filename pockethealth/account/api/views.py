from django.shortcuts import render

from rest_framework import viewsets, filters, status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from account.api.renderers import UserJSONRenderer

from account import models
from account.api import serializers, permissions
from account.models import User, Patient, Practitioner
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Telecom,Link
from account.organization import Organization, OrganizationContact
from account.healthcareService import HealthcareService, HealthcareCategory, Type, Speciality, ServiceProvisionCode, Program,ReferralMethod, availableTime, notAvailableTime
from account.careteam import CareTeam, StatusCode, ParticipantRole, Participant, ReasonCode, Annotation, Author
from account.location import  Location, Status, OperationalStatus, Mode, Types, PhysicalLocationType, Position, HoursOfOperation

from account.api.serializers import PatientRegistrationSerializer, PractitionerRegistrationSerializer, UserLoginSerializer,PeriodSerializer,ContactPointSerializer,DeceasedSerializer,AddressSerializer,HumanNameSerializer,MaritalStatusSerializer,ContactSerializer,CommunicationSerializer,LinkSerializer,TelecomSerializer
from account.api.serializers import OrganizationSerializer,OrganizationContactSerializer,HealthcareServiceSerializer,HealthcareCategorySerializer,TypeSerializer,SpecialitySerializer,ServiceProvisionCodeSerializer,ProgramSerializer,ReferralMethodSerializer,availableTimeSerializer,notAvailableTimeSerializer,CareTeamSerializer,StatusCodeSerializer,ParticipantRoleSerializer,ReasonCodeSerializer,AnnotationSerializer,AuthorSerializer,LocationSerializer,StatusSerializer,OperationalStatusSerializer,ModeSerializer,TypesSerializer,PhysicalLocationTypeSerializer,PositionSerializer,HoursOfOperationSerializer


class PatientRegistration(APIView):
    permission_classes = (AllowAny, )
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = PatientRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception =True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class PractitionerRegistration(APIView):
    permission_classes = (AllowAny, )
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = PractitionerRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception =True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class UserLogin(APIView):
    permission_classes = (AllowAny, )
    # renderer_classes = (UserJSONRenderer, )
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    # permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]

class ContactPointViewSet(viewsets.ModelViewSet):
    queryset = ContactPoint.objects.all()
    serializer_class = ContactPointSerializer

class DeceasedViewSet(viewsets.ModelViewSet):
    queryset = Deceased.objects.all()
    serializer_class = DeceasedSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class HumanNameViewSet(viewsets.ModelViewSet):
    queryset = HumanName.objects.all()
    serializer_class = HumanNameSerializer

class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactPoint.objects.all()
    serializer_class = ContactSerializer

class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer

class TelecomViewSet(viewsets.ModelViewSet):
    queryset = Telecom.objects.all()
    serializer_class = TelecomSerializer

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizationContactViewSet(viewsets.ModelViewSet):
    queryset = OrganizationContact.objects.all()
    serializer_class = OrganizationContactSerializer

class HealthcareServiceViewSet(viewsets.ModelViewSet):
    queryset = HealthcareService.objects.all()
    serializer_class = HealthcareServiceSerializer

class HealthcareCategoryViewSet(viewsets.ModelViewSet):
    queryset = HealthcareCategory.objects.all()
    serializer_class = HealthcareCategorySerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class ServiceProvisionCodeViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvisionCode.objects.all()
    serializer_class = ServiceProvisionCodeSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class ReferralMethodViewSet(viewsets.ModelViewSet):
    queryset = ReferralMethod.objects.all()
    serializer_class = ReferralMethodSerializer

class availableTimeViewSet(viewsets.ModelViewSet):
    queryset = availableTime.objects.all()
    serializer_class = availableTimeSerializer

class notAvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = notAvailableTime.objects.all()
    serializer_class = notAvailableTimeSerializer

class CareTeamViewSet(viewsets.ModelViewSet):
    queryset = CareTeam.objects.all()
    serializer_class = CareTeamSerializer

class StatusCodeViewSet(viewsets.ModelViewSet):
    queryset = StatusCode.objects.all()
    serializer_class = StatusCodeSerializer

class ParticipantRoleViewSet(viewsets.ModelViewSet):
    queryset = ParticipantRole.objects.all()
    serializer_class = ParticipantRoleSerializer

class ReasonCodeViewSet(viewsets.ModelViewSet):
    queryset = ReasonCode.objects.all()
    serializer_class = ReasonCodeSerializer

class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class =LocationSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class OperationalStatusViewSet(viewsets.ModelViewSet):
    queryset = OperationalStatus.objects.all()
    serializer_class = OperationalStatusSerializer

class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer

class TypesViewSet(viewsets.ModelViewSet):
    queryset =Types.objects.all()
    serializer_class =TypesSerializer

class PhysicalLocationTypeViewSet(viewsets.ModelViewSet):
    queryset = PhysicalLocationType.objects.all()
    serializer_class = PhysicalLocationTypeSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class HoursOfOperationViewSet(viewsets.ModelViewSet):
    queryset = HoursOfOperation.objects.all()
    serializer_class = HoursOfOperationSerializer
