import pytest

TEST_DATA = [
    {"name": "yzhtest", "data": {"color": "dark black", "size": "medium"}},
    {"name": "yzhtest2", "data": {"color": "dark black2", "size": "medium2"}}
]

NEGATIVE_DATA = [
    {"name": ["yzhtest"], "data": {"color": "dark black", "size": "medium"}},
    {"name": {"yzhtest2": ''}, "data": {"color": "dark black2", "size": "medium2"}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_post_an_object(obj, create_obj_endpoint, data):
    create_obj_endpoint.check_that_status_is_200()
    create_obj_endpoint.check_response_name_is_correct(data['name'])
    create_obj_endpoint.check_response_color_is_correct(data['data']['color'])
    create_obj_endpoint.check_response_size_is_correct(data['data']['size'])


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_post_an_object_with_negative_data(obj, create_obj_endpoint, data):
    create_obj_endpoint.check_bad_request()


@pytest.mark.parametrize('data', TEST_DATA)
def test_put_an_object(obj, update_obj_endpoint, data):
    payload = {"name": "yzhtestUPD", "data": {"color": "dark blackUPD", "size": "mediumUPD"}}
    update_obj_endpoint.make_changes_in_obj(obj, payload)
    update_obj_endpoint.check_that_status_is_200()
    update_obj_endpoint.check_response_name_is_correct(payload['name'])
    update_obj_endpoint.check_response_color_is_correct(payload['data']['color'])
    update_obj_endpoint.check_response_size_is_correct(payload['data']['size'])


@pytest.mark.parametrize('data', TEST_DATA)
def test_patch_an_object(obj, patch_obj_endpoint, data):
    payload = {"name": "yzhtestPATCH"}
    patch_obj_endpoint.make_changes_in_name_obj(obj, payload)
    patch_obj_endpoint.check_that_status_is_200()
    patch_obj_endpoint.check_response_name_is_correct(payload['name'])
    patch_obj_endpoint.check_response_color_is_correct(data['data']['color'])
    patch_obj_endpoint.check_response_size_is_correct(data['data']['size'])


@pytest.mark.parametrize('data', TEST_DATA)
def test_delete_an_object(obj, delete_obj_endpoint, data):
    delete_obj_endpoint.delete_an_obj(obj)
    delete_obj_endpoint.check_that_status_is_200()
