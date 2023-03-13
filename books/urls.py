from django.urls import path
from .views import (
    BookGeneralView,
    BookEmployeeView,
    BookEmployeeDetailView,
    BookUserDetailView,
)

urlpatterns = [
    path("books/", BookEmployeeView.as_view()),
    path("books/", BookGeneralView.as_view()),
    path("books/<uuid:pk>/", BookEmployeeDetailView.as_view()),
    path("books/<uuid:pk>/", BookUserDetailView.as_view()),
]
