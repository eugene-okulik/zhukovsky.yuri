import requests
import allure

from test_api_yuri_zhukovsky.endpoints.endpoint import Endpoint


class DeleteObj(Endpoint):

    @allure.step('Delete an obj')
    def delete_an_obj(self, obj_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{obj_id}',
            headers=headers
        )

        if self.response.status_code == 200:
            try:
                self.json = self.response.json()
            except ValueError:
                print("\nError: Response is not in JSON format.")
                self.json = None
        else:
            print(f"\nError {self.response.status_code}:\n{self.response.text}")
            self.json = None

        return self.response
