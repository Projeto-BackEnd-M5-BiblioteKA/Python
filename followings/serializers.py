from rest_framework import serializers
from .models import Following


class FollowingSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.ReadOnlyField(source="user.email")

    def create(self, validated_data):
        return Following.objects.create(**validated_data)

    class Meta:
        model = Following
        fields = (
            "id",
            "user",
            "book",
        )

        read_only_fields = ["user"]
