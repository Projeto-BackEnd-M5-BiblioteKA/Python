from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer
from .models import Book
from uuid import uuid4
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser

# Create your views here.


class BookGeneralView(APIView):
    def get(self, request: Request) -> Response:
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookEmployeeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request: Request) -> Response:
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookEmployeeDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def patch(self, request: Request, pk: uuid4) -> Response:
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: uuid4) -> Response:
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
