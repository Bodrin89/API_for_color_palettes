from django.urls import path

from apps.palette.views import (
    CreatePaletteView,
    DeletePaletteView,
    GetPaletteByIdView,
    ListPaletteView,
    UpdatePaletteView,
)

urlpatterns = [
    path('create-palette/', CreatePaletteView.as_view(), name='create-palette'),
    path('list-palette/', ListPaletteView.as_view(), name='list-palette'),
    path('get-palette/<int:pk>/', GetPaletteByIdView.as_view(), name='get-palette_by_id'),
    path('update-palette/<int:pk>/', UpdatePaletteView.as_view(), name='update-palette_by_id'),
    path('destroy-palette/<int:pk>/', DeletePaletteView.as_view(), name='destroy-palette_by_id'),
]
