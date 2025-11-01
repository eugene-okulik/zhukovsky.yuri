import pytest
from test_api_yuri_zhukovsky.endpoints.create_post import CreateObj
from test_api_yuri_zhukovsky.endpoints.delete_post import DeleteObj
from test_api_yuri_zhukovsky.endpoints.patch_post import PatchObj
from test_api_yuri_zhukovsky.endpoints.update_post import UpdateObj


@pytest.fixture()
def create_obj_endpoint():
    return CreateObj()


@pytest.fixture()
def update_obj_endpoint():
    return UpdateObj()


@pytest.fixture()
def patch_obj_endpoint():
    return PatchObj()


@pytest.fixture()
def delete_obj_endpoint():
    return DeleteObj()


@pytest.fixture
def obj(create_obj_endpoint, delete_obj_endpoint, data):
    response = create_obj_endpoint.create_new_obj(payload=data)
    if response.status_code == 200:
        try:
            obj_id = response.json()['id']
            yield obj_id
            delete_obj_endpoint.delete_an_obj(obj_id)
        except ValueError:
            print("\nError: Response is not in JSON format.")
    else:
        print(f"\nError {response.status_code}:\n{response.text}")
        yield response.status_code
