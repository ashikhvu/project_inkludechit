from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,UserProfileModel
from .serializers import UserProfileCreationSerializer
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)