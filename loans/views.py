from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, status, Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .models import Loan
from .serializers import LoanSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class LoanView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanDetailView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request: Request, pk) -> Response:
        
        if request.user.is_collaborator:
            loans = Loan.objects.all()
        else:
            loans = Loan.objects.filter(user=pk)
        
        serealizer = LoanSerializer(loans, many=True)
        return Response(serealizer.data, status.HTTP_200_OK)
    
    def patch(self, request: Request, pk) -> Response:
        loans = get_object_or_404(Loan, id=pk)
        serealizer = LoanSerializer(loans, data=request.data, partial=True)
        serealizer.is_valid(raise_exception=True)

        self.check_object_permissions(request, loans)
        
        serealizer.save()

        return Response(serealizer.data, status.HTTP_200_OK)