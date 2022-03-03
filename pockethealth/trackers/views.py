from django.shortcuts import render
from trackers.api.serializers import BMISerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from trackers.models import BMIData
# Create your views here.

class BMIPost(APIView):
    def post(self, request): 
        serializer = BMISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class BMIFetch(APIView):
    def get(self, request):
        data = BMIData.objects.all()
        serializer = BMISerializer(data, many=True, context={'request': request})
        return Response(serializer.data)

# class StreamPlatformAV(APIView):
#     def get(self, request):
#         platforms = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(platforms, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def post(self, request): 
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
