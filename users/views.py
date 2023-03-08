from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView


class UserView(CreateAPIView):
    queryset = User
    serializer_class = UserSerializer
