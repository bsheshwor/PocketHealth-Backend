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

class PeriodViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,
                     mixins.DestroyModelMixin):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    # permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]

class ContactPointViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,
                     mixins.DestroyModelMixin):
    queryset = ContactPoint.objects.all()
    serializer_class = ContactPointSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class DeceasedViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,
                     mixins.DestroyModelMixin):
    queryset = Deceased.objects.all()
    serializer_class = DeceasedSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AddressViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,
                     mixins.DestroyModelMixin):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class HumanNameViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,
                     mixins.DestroyModelMixin):
    queryset = HumanName.objects.all()
    serializer_class = HumanNameSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class MaritalStatusViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,
                     mixins.DestroyModelMixin):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ContactViewSet(
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,
                     mixins.DestroyModelMixin):
    queryset = ContactPoint.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CommunicationViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,
                     mixins.DestroyModelMixin):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class LinkViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet,
                     mixins.DestroyModelMixin):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)