from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        is_collaborator = validated_data.get("is_collaborator", None)

        if is_collaborator:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)

            setattr(instance, key, value)

        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_blocked",
            "is_collaborator",
        ]
        read_only_fields = ["id", "is_blocked"]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="user with this username already exists.",
                    )
                ]
            },
        }
