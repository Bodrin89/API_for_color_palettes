import pytest
from django.urls import reverse

from config.settings.base import LOGGER


@pytest.mark.django_db
class TestColor:
    def test_color_create(self, client):
        response = client.post('/color/create-color/', data={'hex': '#000000'})
        assert response.status_code == 401

    def test_color_create_auth_user_owner(self, get_auth_client, palette_factory):
        auth_client, user = get_auth_client
        palette_owner = palette_factory(user=user)
        response = auth_client.post('/color/create-color/', data={'hex': '#000000', 'palette': palette_owner.id})
        assert response.status_code == 201

    def test_color_create_auth_user_guest(self, get_auth_client, palette_factory):
        auth_client, user = get_auth_client
        palette_guest = palette_factory()
        response = auth_client.post('/color/create-color/', data={'hex': '#000000', 'palette': palette_guest.id})
        assert response.status_code == 403

    def test_color_list(self, get_auth_client, palette_factory, color_factory):
        auth_client, user = get_auth_client
        palette_owner = palette_factory(user=user)
        color = color_factory(palette=palette_owner)
        palette_factory()

        expected_response = [{'id': color.id, 'hex': color.hex, 'name': color.name, 'palette': palette_owner.id}]
        url = reverse('list-color', kwargs={'palette_id': palette_owner.id})
        response = auth_client.get(path=url)
        LOGGER.info(response.data)

        assert response.status_code == 200
        assert response.data['results'] == expected_response
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['id'] == color.id

    def test_color_get(self, get_auth_client, palette_factory, color_factory):
        auth_client, user = get_auth_client
        palette = palette_factory(user=user)
        color = color_factory(palette=palette)

        expected_response = {'id': color.id, 'hex': color.hex, 'name': color.name, 'palette': palette.id}
        url = reverse('get-color_by_id', kwargs={'pk': color.id})
        response = auth_client.get(path=url)

        assert response.status_code == 200
        assert response.data == expected_response

    def test_color_update_owner(self, get_auth_client, palette_factory, color_factory):
        auth_client, user = get_auth_client
        palette = palette_factory(user=user)
        color = color_factory(palette=palette)
        url = reverse('update-color_by_id', kwargs={'pk': color.id})
        response = auth_client.put(url, data={'hex': '#000000'})

        assert response.status_code == 200

    def test_color_update_guest(self, get_auth_client, palette_factory, color_factory):
        auth_client, user = get_auth_client
        palette = palette_factory()
        color = color_factory(palette=palette)
        url = reverse('update-color_by_id', kwargs={'pk': color.id})
        response = auth_client.put(url, data={'hex': '#000000'})

        assert response.status_code == 404
