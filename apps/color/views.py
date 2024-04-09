from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.color.dao import ColorDAO
from apps.color.permissions import OwnerPermission
from apps.color.serializers import CreateColorSerializer, ListColorSerializer, UpdateColorSerializer


class CreateColorView(generics.CreateAPIView):
    """View для создания цвета"""

    permission_classes = [IsAuthenticated, OwnerPermission]
    serializer_class = CreateColorSerializer
    queryset = ...


class ListColorView(generics.ListAPIView):
    """View для получения списка цветов"""

    permission_classes = (IsAuthenticated,)
    serializer_class = ListColorSerializer

    def get_queryset(self):
        palette_id = self.kwargs.get('palette_id')
        user = self.request.user
        return ColorDAO.list_color_by_id_palette(palette_id, user)


class GetColorByIdView(generics.RetrieveAPIView):
    """View для получения цвета по id"""

    permission_classes = (IsAuthenticated,)
    serializer_class = ListColorSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        color_id = self.kwargs.get('pk')
        return ColorDAO.get_color_by_id(color_id, user_id)


class UpdateColorView(generics.UpdateAPIView):
    """View для обновления цвета"""

    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateColorSerializer
    http_method_names = ['put']

    def get_queryset(self):
        user = self.request.user
        color_id = self.kwargs.get('pk')
        serializer = UpdateColorSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return ColorDAO.get_color_by_id(color_id, user)


class DeleteColorView(generics.DestroyAPIView):
    """View для удаления цвета"""

    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        color_id = self.kwargs.get('pk')
        user = self.request.user
        color = ColorDAO.get_color_by_id(color_id, user)
        if not color:
            return Response(status=status.HTTP_404_NOT_FOUND)
        color.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
