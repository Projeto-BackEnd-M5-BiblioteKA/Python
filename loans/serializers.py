from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):

    def create(self, validated_data: dict) -> Loan:
        return Loan.objects.create(**validated_data)
   
    class Meta:
        model = Loan
        fields = ['id',
                  'created_at',
                  'devolution_date',
                  'is_returned',
                  'book_copy',
                  'user']
