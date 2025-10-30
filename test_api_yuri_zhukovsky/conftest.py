import pytest
from test_api_yuri_zhukovsky.endpoints.create_post import CreatePost
from test_api_yuri_zhukovsky.endpoints.delete_post import DeletePost
from test_api_yuri_zhukovsky.endpoints.patch_post import PatchPost
from test_api_yuri_zhukovsky.endpoints.update_post import UpdatePost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()

@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()

@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()

@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()
