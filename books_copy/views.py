from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .models import BookCopy
from books.models import Book
from .serializers import BookCopySerializer
from rest_framework.views import APIView, status, Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class BookCopyView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request: Request, book_id) -> Response:
        books = get_object_or_404(Book, id=book_id)
        serealizer = BookCopySerializer(data=request.data)
        serealizer.is_valid(raise_exception=True)

        serealizer.save(book=books)

        return Response(serealizer.data, status.HTTP_201_CREATED)
    
    def get(self, request: Request, book_id) -> Response:
        books = BookCopy.objects.filter(book=book_id)
        serealizer = BookCopySerializer(books, many=True)

        return Response(serealizer.data, status.HTTP_200_OK)
# Create your views here.
