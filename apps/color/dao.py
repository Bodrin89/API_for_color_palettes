from apps.color.models import ColorModel


class ColorDAO:
    @staticmethod
    def create_color(data):
        return ColorModel.objects.create(**data)

    @staticmethod
    def get_color_by_id(color_id, user=None):
        if user:
            return ColorModel.objects.select_related('palette', 'palette__user').filter(id=color_id, palette__user=user)
        return ColorModel.objects.get(id=color_id)

    @staticmethod
    def list_color_by_id_palette(palette_id, user_id):
        return ColorModel.objects.select_related('palette', 'palette__user').filter(
            palette__id=palette_id, palette__user_id=user_id
        )
