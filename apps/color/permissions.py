from rest_framework.permissions import BasePermission

from apps.palette.dao import PaletteDAO


class OwnerPermission(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        palette_id = request.data.get('palette')
        palette = PaletteDAO.get_palette_by_id(palette_id=palette_id, user_id=user_id)
        return bool(palette)
