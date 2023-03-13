from rest_framework import serializers
from .models import Book
from books_copy.models import BookCopy

class BookSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=50)
    author = serializers.CharField(required=True, allow_blank=False, max_length=50)
    publication_date = serializers.DateField(required=True)
    summary = serializers.CharField(max_length=127)
    pages = serializers.IntegerField()
    copies_quantity = serializers.IntegerField()
    is_available = serializers.BooleanField()

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        for i in range(validated_data['copies_quantity']):
            BookCopy.objects.create(book=book)
        return book
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publication_date', 'summary', 'pages', 'copies_quantity', 'is_available')