from rest_framework import serializers

from apps.palette.dao import PaletteDAO
from apps.palette.models import PaletteModel


class CreatePaletteSerializer(serializers.ModelSerializer):
    """Сериализатор для создания палитры"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PaletteModel
        fields = ('id', 'name', 'user')

    def create(self, validated_data):
        return PaletteDAO.create_palette(validated_data)


class ListPaletteSerializer(serializers.ModelSerializer):
    """Сериализатор для получения списка палитр пользователя"""

    class Meta:
        model = PaletteModel
        fields = ('id', 'name', 'user')


class UpdatePaletteSerializer(serializers.ModelSerializer):
    """Сериализатор для обновления палитры"""

    class Meta:
        model = PaletteModel
        fields = ('id', 'name')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
