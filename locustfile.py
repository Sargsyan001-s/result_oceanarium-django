from faker import Faker
from locust import HttpUser, TaskSet, task, between
import random

fake = Faker("ru_RU")


class SiteTests(TaskSet):
    @task(5)
    def products(self):
        self.client.get("/products/")

    @task(5)
    def categories(self):
        self.client.get("/categories/")

    @task(5)
    def about(self):
        self.client.get("/about/")

    @task(5)
    def aquariums(self):
        self.client.get("/aquariums/")

    @task(1)
    def registration(self):
        page = self.client.get("/registration/")
        token = page.cookies.get("csrftoken")
        password = "Test_" + str(random.randint(1000, 9999)) + "a"
        self.client.post("/registration/", data={
            "username": fake.user_name() + str(random.randint(10, 9999)),
            "email": fake.email(domain="mpt.ru"),
            "password1": password,
            "password2": password,
            "csrfmiddlewaretoken": token,
        }, headers={"X-CSRFToken": token})


class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = between(1, 2)
    tasks = [SiteTests]
