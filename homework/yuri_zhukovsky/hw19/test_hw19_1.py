import pytest
import requests


@pytest.fixture()
def new_object():
    body = {
        "name": "yzhtest",
        "data": {
            "color": "dark black",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    obj_id = response.json()['id']
    yield obj_id, response
    requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')


def test_post_an_object(new_object):
    obj_id, response = new_object
    assert isinstance(response.json()['id'], int), 'ID is not an integer'
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'yzhtest', 'Name is incorrect'
    assert response.json()['data']['color'] == 'dark black', 'Color is incorrect'
    assert response.json()['data']['size'] == 'medium', 'Size is incorrect'


def test_put_an_object(new_object):
    obj_id, response = new_object
    body = {
        "name": "zhtest",
        "data": {
            "color": "white",
            "size": "big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{obj_id}',
        json=body,
        headers=headers
    )
    assert isinstance(response.json()['id'], int), 'ID is not an integer'
    assert response.json()['id'] == obj_id, 'ID is incorrect'
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'zhtest', 'Name is incorrect'
    assert response.json()['data']['color'] == 'white', 'Color is incorrect'
    assert response.json()['data']['size'] == 'big', 'Size is incorrect'


def test_patch_an_object(new_object):
    obj_id, response = new_object
    body = {
        "name": "zhprod"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{obj_id}',
        json=body,
        headers=headers
    )
    assert isinstance(response.json()['id'], int), 'ID is not an integer'
    assert response.json()['id'] == obj_id, 'ID is incorrect'
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'zhprod', 'Name is incorrect'
    assert response.json()['data']['color'] == 'dark black', 'Color is incorrect'
    assert response.json()['data']['size'] == 'medium', 'Size is incorrect'


def test_delete_an_object(new_object):
    obj_id, response = new_object
    response = requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.content.decode(
        'utf-8') == f'Object with id {obj_id} successfully deleted', 'Message is incorrect'
