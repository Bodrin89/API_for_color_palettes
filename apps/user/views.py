from rest_framework import generics

from apps.user.serializers import UserCreateSerializer


class UserCreateView(generics.CreateAPIView):
    """View для создания пользователя"""

    serializer_class = UserCreateSerializer
    queryset = ...
