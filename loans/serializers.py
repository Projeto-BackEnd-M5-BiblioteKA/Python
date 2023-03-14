from rest_framework import serializers
from .models import Loan
from datetime import date
from rest_framework.exceptions import ValidationError


class LoanSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Loan:
        today = date.today()
        book_copy = validated_data["book_copy"]
        user = validated_data["user"]
        active_loans = Loan.objects.filter(user=user, is_returned=False)
        active_loans_date = active_loans and Loan.objects.filter(
            user=user, devolution_date__lt=today, is_returned = False
        )

        if active_loans_date.exists():
            user.is_blocked = True
            user.save()

            raise ValidationError(
                "User has exceeded the return time for a borrowed copy and is blocked until it is returned."
            )

        if active_loans.count() >= 3:
            raise ValidationError("User has 3 active loans.")

        if book_copy.is_borrowed:
            raise ValidationError("This book copy is already borrowed.")

        book_copy.is_borrowed = True
        book_copy.save()

        return Loan.objects.create(**validated_data)

    class Meta:
        model = Loan
        fields = [
            "id",
            "created_at",
            "devolution_date",
            "is_returned",
            "book_copy",
            "user",
        ]

        read_only_fields = ["created_at", "devolution_date", "is_returned"]
