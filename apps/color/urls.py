from django.urls import path

from apps.color.views import CreateColorView, DeleteColorView, GetColorByIdView, ListColorView, UpdateColorView

urlpatterns = [
    path('create-color/', CreateColorView.as_view(), name='create-color'),
    path('list-color/<int:palette_id>/', ListColorView.as_view(), name='list-color'),
    path('get-color/<int:pk>/', GetColorByIdView.as_view(), name='get-color_by_id'),
    path('update-color/<int:pk>/', UpdateColorView.as_view(), name='update-color_by_id'),
    path('destroy-color/<int:pk>/', DeleteColorView.as_view(), name='destroy-color_by_id'),
]
