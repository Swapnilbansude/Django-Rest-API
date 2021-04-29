from django.shortcuts import render
from . models import User
from rest_framework.permissions import IsAuthenticated
from . serializers import UserSerializer
from rest_framework.generics import (ListCreateAPIView)
from rest_framework import generics 


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]