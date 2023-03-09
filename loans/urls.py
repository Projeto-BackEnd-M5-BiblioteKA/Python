from django.urls import path, include
from .views import LoanView, LoanDetailView, LoanUserDetailView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("loans/", LoanView.as_view()),
    path("loans/<int:loan_id>/", LoanDetailView.as_view()),
    path("loans/<int:user_id>/", LoanUserDetailView.as_view()),
]
