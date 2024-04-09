from apps.palette.models import PaletteModel


class PaletteDAO:
    @staticmethod
    def create_palette(data):
        return PaletteModel.objects.select_related('user').create(**data)

    @staticmethod
    def get_palette_by_user(user_id):
        return PaletteModel.objects.select_related('user').filter(user=user_id)

    @staticmethod
    def get_palette_by_id(palette_id, user_id):
        return PaletteModel.objects.select_related('user').filter(id=palette_id, user_id=user_id)
