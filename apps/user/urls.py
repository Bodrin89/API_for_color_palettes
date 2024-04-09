from django.urls import path

from apps.user.views import UserCreateView

urlpatterns = [
    path('create-users/', UserCreateView.as_view(), name='create-users'),
]
