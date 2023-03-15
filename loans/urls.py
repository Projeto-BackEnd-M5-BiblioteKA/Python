from django.urls import path
from .views import LoanView, LoanDetailViewGet, LoanDetailViewUpdate

urlpatterns = [
    path("books/loans/", LoanView.as_view()),
    path("books/loans/<uuid:pk>/", LoanDetailViewGet.as_view()),
    path("books/loans/<uuid:pk>/update/", LoanDetailViewUpdate.as_view()),
]
