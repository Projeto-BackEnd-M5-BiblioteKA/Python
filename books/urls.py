from django.urls import path
from .views import BookGeneralView, BookEmployeeView, BookEmployeeDetailView

urlpatterns = [
    path("books/", BookGeneralView.as_view()),
    path("books/employee/", BookEmployeeView.as_view()),
    path("books/employee/<uuid:pk>/", BookEmployeeDetailView.as_view()),
]