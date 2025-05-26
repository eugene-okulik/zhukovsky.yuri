import requests


def post_an_object():
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
    # print(response.json()['id'])
    clear_an_object(response.json()['id'])
    assert isinstance(response.json()['id'], int), 'ID is not an integer'
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'yzhtest', 'Name is incorrect'
    assert response.json()['data']['color'] == 'dark black', 'Color is incorrect'
    assert response.json()['data']['size'] == 'medium', 'Size is incorrect'


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
    # print(response.json()['id'])
    return response.json()['id']


def clear_an_object(obj_id):
    requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')


def put_an_object():
    obj_id = new_object()
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
    clear_an_object(obj_id)
    assert isinstance(response.json()['id'], int), 'ID is not an integer'
    # # print(response.json())
    assert response.json()['id'] == obj_id, 'ID is incorrect'
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'zhtest', 'Name is incorrect'
    assert response.json()['data']['color'] == 'white', 'Color is incorrect'
    assert response.json()['data']['size'] == 'big', 'Size is incorrect'


def patch_an_object():
    obj_id = new_object()
    body = {
        "name": "zhprod"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{obj_id}',
        json=body,
        headers=headers
    )
    clear_an_object(obj_id)
    assert isinstance(response.json()['id'], int), 'ID is not an integer'
    # print(response.json())
    assert response.json()['id'] == obj_id, 'ID is incorrect'
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'zhprod', 'Name is incorrect'
    assert response.json()['data']['color'] == 'dark black', 'Color is incorrect'
    assert response.json()['data']['size'] == 'medium', 'Size is incorrect'


def delete_an_object():
    obj_id = new_object()
    response = requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')
    # print(response.status_code)
    # print(response.content)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.content.decode(
        'utf-8') == f'Object with id {obj_id} successfully deleted', 'Message is incorrect'


post_an_object()
put_an_object()
patch_an_object()
delete_an_object()
