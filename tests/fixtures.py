import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def get_auth_client(client: APIClient, user_factory):
    user = user_factory()
    client.force_authenticate(user)
    return client, user
