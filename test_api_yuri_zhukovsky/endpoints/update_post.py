import requests
import allure

from test_api_yuri_zhukovsky.endpoints.endpoint import Endpoint


class UpdateObj(Endpoint):

    @allure.step('Update an obj')
    def make_changes_in_obj(self, obj_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{obj_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
