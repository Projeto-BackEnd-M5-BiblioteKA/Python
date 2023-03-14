from rest_framework import generics
from rest_framework.views import APIView, status, Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Loan
from .serializers import LoanSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
from .permissions import CustomLoansPermissions

# Create your views here.


class LoanView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomLoansPermissions]

    def get(self, request: Request, pk) -> Response:
        is_collaborator = request.user.is_collaborator

        print(request.user.username)

        if pk != request.user.id and not is_collaborator:
            raise ValidationError(
                "You don't have permissions, you not collaborator and can list only yourself loans."
            )

        if is_collaborator:
            loans = Loan.objects.all()
        else:
            loans = Loan.objects.filter(user=pk)

        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, pk) -> Response:
        loans = get_object_or_404(Loan, id=pk)
        loans.is_returned = True
        serializer = LoanSerializer(loans, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.check_object_permissions(request, loans)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
