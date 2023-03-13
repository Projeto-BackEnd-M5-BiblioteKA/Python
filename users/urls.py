from django.urls import path
from .views import UserView, UserViewDetail
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<uuid:pk>/", UserViewDetail.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
