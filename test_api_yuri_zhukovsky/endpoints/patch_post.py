import requests
import allure

from test_api_yuri_zhukovsky.endpoints.endpoint import Endpoint


class PatchObj(Endpoint):

    @allure.step('Patch an obj')
    def make_changes_in_name_obj(self, obj_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{obj_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
