from djoser.serializers import UserCreateSerializer
from .models import *
from rest_framework import serializers
from . models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','first_name','last_name','phone','username',
                        'aadhar_no','address','email','is_admin','category','password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','phone','username',
                        'aadhar_no','address','email','is_admin','category','password')