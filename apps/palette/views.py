from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.palette.dao import PaletteDAO
from apps.palette.serializers import CreatePaletteSerializer, ListPaletteSerializer, UpdatePaletteSerializer


class CreatePaletteView(generics.CreateAPIView):
    """View для создания палитры"""

    permission_classes = (IsAuthenticated,)
    serializer_class = CreatePaletteSerializer
    queryset = ...


class ListPaletteView(generics.ListAPIView):
    """View для получения списка палитр пользователя"""

    permission_classes = (IsAuthenticated,)
    serializer_class = ListPaletteSerializer

    def get_queryset(self):
        user = self.request.user
        return PaletteDAO.get_palette_by_user(user)


class GetPaletteByIdView(generics.RetrieveAPIView):
    """View для получения палитры по id"""

    permission_classes = (IsAuthenticated,)
    serializer_class = ListPaletteSerializer

    def get_queryset(self):
        palette_id = self.kwargs.get('pk')
        user = self.request.user
        return PaletteDAO.get_palette_by_id(palette_id, user)


class UpdatePaletteView(generics.UpdateAPIView):
    """View для обновления палитры"""

    permission_classes = (IsAuthenticated,)
    serializer_class = UpdatePaletteSerializer
    http_method_names = ['put']

    def get_queryset(self):
        palette_id = self.kwargs.get('pk')
        user = self.request.user
        return PaletteDAO.get_palette_by_id(palette_id, user)


class DeletePaletteView(generics.DestroyAPIView):
    """View для удаления палитры"""

    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        palette_id = self.kwargs.get('pk')
        user = self.request.user
        palette = PaletteDAO.get_palette_by_id(palette_id, user)
        if not palette:
            return Response(status=status.HTTP_404_NOT_FOUND)
        palette.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
