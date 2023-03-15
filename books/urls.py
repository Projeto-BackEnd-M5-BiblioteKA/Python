from django.urls import path
from .views import (
    BookGeneralView,
    BookEmployeeView,
    BookEmployeeDetailViewUpdate,
    BookEmployeeDetailViewDestroy,
)

urlpatterns = [
    path("books/", BookGeneralView.as_view()),
    path("books/employee/", BookEmployeeView.as_view()),
    path("books/employee/<uuid:pk>/update/", BookEmployeeDetailViewUpdate.as_view()),
    path("books/employee/<uuid:pk>/delete/", BookEmployeeDetailViewDestroy.as_view()),
]
