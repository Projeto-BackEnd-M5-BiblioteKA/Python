from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .models import BookCopy
from books.models import Book
from .serializers import BookCopySerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView


class BookCopyView(ListCreateAPIView, PageNumberPagination):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        book_id = self.kwargs.get("book_id")
        return BookCopy.objects.filter(book=book_id)

    def perform_create(self, serializer):
        book_id = self.kwargs.get("book_id")
        book = get_object_or_404(Book, id=book_id)
        serializer.save(book=book)


# Create your views here.
