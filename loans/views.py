from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .models import Loan
from .serializers import LoanSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
from .permissions import CustomLoansPermissions

# Create your views here.


class LoanView(ListCreateAPIView, PageNumberPagination):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]


class LoanDetailViewGet(ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomLoansPermissions]

    def get_queryset(self):
        is_collaborator = self.request.user.is_collaborator
        user_id = self.kwargs.get("pk", None)

        print(user_id, self.request.user.id)

        if user_id != self.request.user.id and not is_collaborator:
            raise ValidationError(
                "You don't have permissions, you not collaborator and can list only yourself loans."
            )

        if is_collaborator:
            return Loan.objects.all()

        return Loan.objects.filter(user=user_id)


class LoanDetailViewUpdate(UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
