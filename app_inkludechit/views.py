from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,UserProfileModel,my_model
from .serializers import UserProfileCreationSerializer,MyModelSerializer
from rest_framework import status
from django.http import JsonResponse

# Create your views here.
class IndexView(APIView):
    def get(self, request):
        profile = UserProfileModel.objects.all()
        serializer = UserProfileCreationSerializer(profile, many=True)
        return JsonResponse(serializer.data,safe=False)

    def post(self, request):
        serializer = UserProfileCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED,safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST,safe=False)
    
class MymodelView(APIView):
    def get(self,request):
        mymdoel = my_model.objects.all()
        serializer = MyModelSerializer(many=True)
        return JsonResponse(serializer.data,safe=False)
    
    def post(self,request):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"success":"Data Saved Successfully"},safe=False)
        return JsonResponse({"error":"Data Submission failed"},safe=False)
        
    
class MymodelSingleView(APIView):
    def get(self,request,pk):
        mymdoel = my_model.objects.get(id=pk)
        serializer = MyModelSerializer(mymdoel,many=False)
        return JsonResponse(serializer.data,safe=False)