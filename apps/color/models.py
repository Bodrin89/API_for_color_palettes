from django.db import models

from apps.palette.models import PaletteModel


class ColorModel(models.Model):
    """Модель цвета"""

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        db_table = 'color_color'

    hex = models.CharField(max_length=7, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    palette = models.ForeignKey(PaletteModel, on_delete=models.CASCADE, null=True, blank=True, related_name='colors')
