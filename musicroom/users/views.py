import json
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import views

# def profile(request):
#     User = get_user_model()
#     user = User.objects.all()
#     user_json = json.dumps(user)
#     return HttpResponse(user_json)


class UserProfileView(views.APIView):
    def get(self, request, format=None):
        user_profile = UserProfile.objects.get(pk=request.user.id)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)
