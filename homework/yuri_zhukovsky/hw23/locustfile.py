from locust import task, HttpUser


class ObjUser(HttpUser):

    headers = {'Content-Type': 'application/json'}
    obj_id = None
    ids = []

    @task(3)
    def add_one_obj(self):
        response = self.client.post(
            '/object',
            json={"name": "yzhtest", "data": {"color": "dark black", "size": "medium"}},
            headers=self.headers
        )
        self.obj_id = response.json()['id']
        self.ids.append(self.obj_id)

    @task(2)
    def get_all_obj(self):
        self.client.get(
            '/object',
            headers=self.headers
        )

    @task(3)
    def get_one_obj(self):
        self.client.get(
            f'/object/{self.ids[0]}',
            headers=self.headers
        )

    @task(1)
    def put_one_obj(self):
        self.client.put(
            f'/object/{self.ids[0]}',
            json={"name": "yzhtestUPD", "data": {"color": "dark blackUPD", "size": "mediumUPD"}},
            headers=self.headers
        )

    @task(1)
    def patch_one_obj(self):
        self.client.patch(
            f'/object/{self.ids[0]}',
            json={"name": "yzhtestPATCH"},
            headers=self.headers
        )

    @task(1)
    def delete_one_obj(self):
        self.client.delete(
            f'/object/{self.ids[0]}',
            headers=self.headers
        )
        self.ids.pop(0)
