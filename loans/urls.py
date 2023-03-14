from django.urls import path, include
from .views import LoanView, LoanDetailView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("books/loans/", LoanView.as_view()),
    path("books/loans/<uuid:pk>", LoanDetailView.as_view()),
]
