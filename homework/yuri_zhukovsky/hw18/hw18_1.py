import requests
import allure


@allure.feature('Posts')
@allure.story('Post creation')
@allure.title('POST request')
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
    clear_an_object(response.json()['id'])
    with allure.step('Asserts'):
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
    return response.json()['id']


def clear_an_object(obj_id):
    requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')


@allure.feature('Posts')
@allure.story('Post edit')
@allure.title('PUT request')
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
    with allure.step('Asserts'):
        assert isinstance(response.json()['id'], int), 'ID is not an integer'
        assert response.json()['id'] == obj_id, 'ID is incorrect'
        assert response.status_code == 200, 'Status code is incorrect'
        assert response.json()['name'] == 'zhtest', 'Name is incorrect'
        assert response.json()['data']['color'] == 'white', 'Color is incorrect'
        assert response.json()['data']['size'] == 'big', 'Size is incorrect'


@allure.feature('Posts')
@allure.story('Post edit name')
@allure.title('PATCH request')
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
    with allure.step('Asserts'):
        assert isinstance(response.json()['id'], int), 'ID is not an integer'
        assert response.json()['id'] == obj_id, 'ID is incorrect'
        assert response.status_code == 200, 'Status code is incorrect'
        assert response.json()['name'] == 'zhprod', 'Name is incorrect'
        assert response.json()['data']['color'] == 'dark black', 'Color is incorrect'
        assert response.json()['data']['size'] == 'medium', 'Size is incorrect'


@allure.feature('Posts')
@allure.story('Post deletion')
@allure.title('DELETE request')
def delete_an_object():
    obj_id = new_object()
    response = requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')
    with allure.step('Asserts'):
        assert response.status_code == 200, 'Status code is incorrect'
        assert response.content.decode(
        'utf-8') == f'Object with id {obj_id} successfully deleted', 'Message is incorrect'


post_an_object()
put_an_object()
patch_an_object()
delete_an_object()
