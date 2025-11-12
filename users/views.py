from django.shortcuts import render

# Create your views here.
# users/views.py
from rest_framework import generics, status
from .serializers import RegisterSerializer
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []  
