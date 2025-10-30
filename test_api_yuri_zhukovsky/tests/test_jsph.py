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
def test_post_an_object_new(create_post_endpoint, delete_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_response_name_is_correct(data['name'])
    create_post_endpoint.check_response_color_is_correct(data['data']['color'])
    create_post_endpoint.check_response_size_is_correct(data['data']['size'])
    post_id = create_post_endpoint.json['id']
    delete_post_endpoint.delete_a_post(post_id)


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_post_with_negative_data(create_post_endpoint, data):
    create_post_endpoint.create_new_post(data)
    create_post_endpoint.check_bad_request()


@pytest.mark.parametrize('data', TEST_DATA)
def test_put_a_post(create_post_endpoint, delete_post_endpoint, update_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    post_id = create_post_endpoint.json['id']
    payload = {"name": "yzhtestUPD", "data": {"color": "dark blackUPD", "size": "mediumUPD"}}
    update_post_endpoint.make_changes_in_post(post_id, payload)
    update_post_endpoint.check_that_status_is_200()
    update_post_endpoint.check_response_name_is_correct(payload['name'])
    update_post_endpoint.check_response_color_is_correct(payload['data']['color'])
    update_post_endpoint.check_response_size_is_correct(payload['data']['size'])
    delete_post_endpoint.delete_a_post(post_id)


@pytest.mark.parametrize('data', TEST_DATA)
def test_patch_a_post(create_post_endpoint, delete_post_endpoint, patch_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    post_id = create_post_endpoint.json['id']
    payload = {"name": "yzhtestPATCH"}
    patch_post_endpoint.make_changes_in_name_post(post_id, payload)
    patch_post_endpoint.check_that_status_is_200()
    patch_post_endpoint.check_response_name_is_correct(payload['name'])
    patch_post_endpoint.check_response_color_is_correct(data['data']['color'])
    patch_post_endpoint.check_response_size_is_correct(data['data']['size'])
    delete_post_endpoint.delete_a_post(post_id)


@pytest.mark.parametrize('data', TEST_DATA)
def test_delete_a_post(create_post_endpoint, delete_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    post_id = create_post_endpoint.json['id']
    delete_post_endpoint.delete_a_post(post_id)
    delete_post_endpoint.check_that_status_is_200()
