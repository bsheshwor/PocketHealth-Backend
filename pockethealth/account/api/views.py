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
from account.models import User, Customer, Doctor,Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Link

from account.api.serializers import CustomerRegistrationSerializer, DoctorRegistrationSerializer, UserLoginSerializer,PeriodSerializer,ContactPointSerializer,DeceasedSerializer,AddressSerializer,HumanNameSerializer,MaritalStatusSerializer,ContactSerializer,CommunicationSerializer,LinkSerializer

class CustomerRegistration(APIView):
    permission_classes = (AllowAny, )
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = CustomerRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception =True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class DoctorRegistration(APIView):
    permission_classes = (AllowAny, )
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = DoctorRegistrationSerializer

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

class PeriodViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    # permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]

class ContactPointViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = ContactPoint.objects.all()
    serializer_class = ContactPointSerializer

class DeceasedViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Deceased.objects.all()
    serializer_class = DeceasedSerializer

class AddressViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class HumanNameViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = HumanName.objects.all()
    serializer_class = HumanNameSerializer

class MaritalStatusViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer

class ContactViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = ContactPoint.objects.all()
    serializer_class = ContactSerializer

class CommunicationViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer

class LinkViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer