import requests
import allure

from test_api_yuri_zhukovsky.endpoints.endpoint import Endpoint


class DeletePost(Endpoint):


    @allure.step('Delete a post')
    def delete_a_post(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{post_id}',
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
