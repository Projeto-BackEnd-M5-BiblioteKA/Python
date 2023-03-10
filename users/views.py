from .models import User
from .serializers import UserSerializer
from .permissions import CustomUserPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomUserPermissions]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return User.objects.all()

        return User.objects.filter(id=user.id)


class UserViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_destroy(self, instance):
        instance.is_blocked = True
        instance.save()
