from locust import HttpUser, task


class ProtoappUser(HttpUser):
    host = 'http://localhost:8000'

    @task
    def hello_word(self):
        self.client.get('/home')

    @task
    def get_item(self):
        self.client.get("/item")
