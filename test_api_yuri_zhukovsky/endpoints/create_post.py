import requests
import allure

from test_api_yuri_zhukovsky.endpoints.endpoint import Endpoint


class CreateObj(Endpoint):

    @allure.step('Create new obj')
    def create_new_obj(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )

        if self.response.status_code == 200:
            try:
                self.json = self.response.json()
            except ValueError:
                print("\nResponse is not in JSON format.")
                self.json = None
        else:
            print(f"\nError {self.response.status_code}:\n{self.response.text}")
            self.json = None

        return self.response
