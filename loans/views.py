from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, status, Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Loan
from .serializers import LoanSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class LoanView(generics.ListCreateAPIView, PageNumberPagination):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanDetailView(generics.RetrieveUpdateAPIView, PageNumberPagination):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanUserDetailView(APIView):
    def get(self, request: Request, user_id) -> Response:
        loans = get_object_or_404(Loan, user=user_id)

        serealizer = LoanSerializer(loans)

        return Response(serealizer.data, status.HTTP_200_OK)
