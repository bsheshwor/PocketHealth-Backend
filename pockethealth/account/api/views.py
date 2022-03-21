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
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Link

from account.api.serializers import PatientRegistrationSerializer, PractitionerRegistrationSerializer, UserLoginSerializer,PeriodSerializer,ContactPointSerializer,DeceasedSerializer,AddressSerializer,HumanNameSerializer,MaritalStatusSerializer,ContactSerializer,CommunicationSerializer,LinkSerializer

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

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
