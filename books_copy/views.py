from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import BookCopy
from .serializers import BookCopySerializer
from rest_framework.pagination import PageNumberPagination


class BookCopyView(generics.CreateAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

    def perform_create(self, serializer, pk):
        print(self.request)
        return serializer.save(book=self.request.content_params.pk)
# Create your views here.
