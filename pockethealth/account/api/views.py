from django.shortcuts import render

from rest_framework import viewsets, filters, status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from account.api.renderers import UserJSONRenderer

from account import models
from account.api import serializers, permissions
from account.api.serializers import CustomerRegistrationSerializer, DoctorRegistrationSerializer, UserLoginSerializer

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
