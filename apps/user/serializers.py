from rest_framework import serializers

from apps.user.dao import UserDAO
from apps.user.models import UserModel


class UserCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания пользователя."""

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ('login', 'username', 'password')

    def create(self, validated_data):
        return UserDAO.create_user(validated_data)
