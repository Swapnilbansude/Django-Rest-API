from django.urls import path, include
from webapi import views 
from . views import UserList

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('allusers/', UserList.as_view()),
]