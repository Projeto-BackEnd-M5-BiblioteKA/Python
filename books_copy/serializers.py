from rest_framework import serializers
from .models import BookCopy


class BookCopySerializer(serializers.ModelSerializer):

    def create(self, validated_data: dict) -> BookCopy:
        return BookCopy.objects.create(**validated_data)

    class Meta:
        model = BookCopy
        fields = ['id',
                  'is_borrowed',
                  'book']
