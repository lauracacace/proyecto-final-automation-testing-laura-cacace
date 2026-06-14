import pytest

from src.utils.api_client import APIClient


client = APIClient()


@pytest.mark.api
def test_get_posts_list():
    resp = client.get('/posts', params={'userId': 1})
    assert resp.status_code == 200
    body = resp.json()
    assert isinstance(body, list)
    assert len(body) > 0


@pytest.mark.api
def test_create_post():
    payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
    resp = client.post('/posts', json=payload)
    assert resp.status_code == 201
    body = resp.json()
    assert body.get('title') == payload['title']
    assert 'id' in body


@pytest.mark.api
def test_delete_post():
    # JSONPlaceholder returns 200 on delete
    resp = client.delete('/posts/1')
    assert resp.status_code in (200, 204)
