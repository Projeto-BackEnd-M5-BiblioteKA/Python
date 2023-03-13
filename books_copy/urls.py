from django.urls import path, include
from .views import BookCopyView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("books/<int:pk>/copy", BookCopyView.as_view()),
]
