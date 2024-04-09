from rest_framework import serializers

from apps.color.models import ColorModel

from .tasks import fetch_and_save_color_name


class CreateColorSerializer(serializers.ModelSerializer):
    """Сериализатор для создания цвета"""

    class Meta:
        model = ColorModel
        fields = ('id', 'hex', 'palette')

    def create(self, validated_data):
        hex_value = validated_data.get('hex')
        color = super().create(validated_data)
        fetch_and_save_color_name.delay(hex_value, color.id)
        return color


class ListColorSerializer(serializers.ModelSerializer):
    """Сериализатор для получения списка цветов палитры пользователя"""

    class Meta:
        model = ColorModel
        fields = ('id', 'hex', 'name', 'palette')


class UpdateColorSerializer(serializers.ModelSerializer):
    """Сериализатор для обновления цвета"""

    hex = serializers.CharField(max_length=7, required=False)

    class Meta:
        model = ColorModel
        fields = ('id', 'hex')

    def update(self, instance, validated_data):
        hex_value = validated_data.get('hex', instance.hex)
        if hex_value:
            color_id = self.data.get('id')
            fetch_and_save_color_name.delay(hex_value, color_id)
        instance.hex = hex_value
        instance.save()
        return instance
