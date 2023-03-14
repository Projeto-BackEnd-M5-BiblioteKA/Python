from rest_framework import serializers
from .models import Book
from books_copy.models import BookCopy


class BookSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        book = Book.objects.create(**validated_data)

        for _ in range(validated_data["copies_quantity"]):
            BookCopy.objects.create(book=book)
        return book

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "publication_date",
            "summary",
            "pages",
            "copies_quantity",
            "is_available",
        ]

        read_only_fields = ["is_available"]
