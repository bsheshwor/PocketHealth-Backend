from django.shortcuts import render
from trackers.api.serializers import BMISerializer, PressureSerializer, BloodSugarSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from trackers.models import BMIData, PressureData, BloodSugarData
from rest_framework import viewsets
# Create your views here.

class BmiVS(viewsets.ModelViewSet):
    queryset = BMIData.objects.all()
    serializer_class = BMISerializer

class PressureVS(viewsets.ModelViewSet):
    queryset = PressureData.objects.all()
    serializer_class = PressureSerializer

class BloodSugarVS(viewsets.ModelViewSet):
    queryset = BloodSugarData.objects.all()
    serializer_class = BloodSugarSerializer


    # def post(self, request): 
    #     serializer = BMISerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)

# class BMIFetch(APIView):
#     def get(self, request):
#         data = BMIData.objects.all()
#         serializer = BMISerializer(data, many=True, context={'request': request})
#         return Response(serializer.data)
