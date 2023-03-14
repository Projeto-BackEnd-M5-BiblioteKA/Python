from rest_framework import serializers
from .models import BookCopy


class BookCopySerializer(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField()

    def get_book_title(self, obj):
        return obj.book.title

    class Meta:
        model = BookCopy
        fields = ["id", "book_title", "book", "is_borrowed"]
        read_only_fields = ["book_title"]
