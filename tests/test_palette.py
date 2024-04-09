import pytest


@pytest.mark.django_db
class TestPalette:
    def test_palette_create(self, client):
        response = client.post('/palette/create-palette/', data={'name': 'test'})
        assert response.status_code == 401

    def test_palette_create_auth_user(self, get_auth_client):
        auth_client, user = get_auth_client
        response = auth_client.post('/palette/create-palette/', data={'name': 'test'})

        assert response.data['name'] == 'test'
        assert response.status_code == 201

    def test_palette_list(self, get_auth_client, palette_factory):
        auth_client, user = get_auth_client
        palette_owner = palette_factory(user=user)
        palette_factory()

        expected_response = [{'id': palette_owner.id, 'name': palette_owner.name, 'user': palette_owner.user.id}]

        response = auth_client.get('/palette/list-palette/')

        assert response.data['results'] == expected_response
        assert len(response.data['results']) == 1
        assert response.status_code == 200

    def test_palette_update_owner(self, get_auth_client, palette_factory):
        auth_client, user = get_auth_client
        palette = palette_factory(user=user)
        response = auth_client.put(f'/palette/update-palette/{palette.id}/', data={'name': 'test'})
        assert response.data['name'] == 'test'
        assert response.status_code == 200

    def test_palette_update_guest(self, get_auth_client, palette_factory):
        auth_client, user = get_auth_client
        palette = palette_factory()
        response = auth_client.put(f'/palette/update-palette/{palette.id}/', data={'name': 'test'})
        assert response.status_code == 404

    def test_palette_destroy_owner(self, get_auth_client, palette_factory):
        auth_client, user = get_auth_client
        palette = palette_factory(user=user)
        response = auth_client.delete(f'/palette/destroy-palette/{palette.id}/')
        assert response.status_code == 204

    def test_palette_destroy_guest(self, get_auth_client, palette_factory):
        auth_client, user = get_auth_client
        palette = palette_factory()
        response = auth_client.delete(f'/palette/destroy-palette/{palette.id}/')
        assert response.status_code == 404

    def test_palette_get_owner(self, get_auth_client, palette_factory):
        auth_client, user = get_auth_client
        palette_owner = palette_factory(user=user)

        expected_response = {'id': palette_owner.id, 'name': palette_owner.name, 'user': palette_owner.user.id}
        response = auth_client.get(f'/palette/get-palette/{palette_owner.id}/')
        assert response.data == expected_response
        assert response.status_code == 200

    def test_palette_get_guest(self, get_auth_client, palette_factory):
        auth_client, user = get_auth_client
        palette = palette_factory()
        response = auth_client.get(f'/palette/get-palette/{palette.id}/')
        assert response.status_code == 404
