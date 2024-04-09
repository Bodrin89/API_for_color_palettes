from django.db import models

from apps.user.models import UserModel


class PaletteModel(models.Model):
    """Модель палитры."""

    class Meta:
        verbose_name = 'Палитра'
        verbose_name_plural = 'Палитры'
        db_table = 'palette_palette'

    name = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='palettes')
