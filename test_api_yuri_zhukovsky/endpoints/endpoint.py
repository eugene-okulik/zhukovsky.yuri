import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}


    @allure.step('Check the name is the same as sent')
    def check_response_name_is_correct(self, expected_name):
        assert self.json['name'] == expected_name, f"Expected name {expected_name}, but got {self.json['name']}"

    @allure.step('Check the color is the same as sent')
    def check_response_color_is_correct(self, expected_color):
        assert (self.json['data']['color'] == expected_color), (f"Expected color {expected_color}, "
                                                                f"but got {self.json['data']['color']}")

    @allure.step('Check the size is the same as sent')
    def check_response_size_is_correct(self, expected_size):
        assert (self.json['data']['size'] == expected_size), (f"Expected color {expected_size}, "
                                                              f"but got {self.json['data']['size']}")

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, f"Expected status code 200, but got {self.response.status_code}"

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert int(self.response.status_code) == 400, f"Expected status code 400, but got {self.response.status_code}"
