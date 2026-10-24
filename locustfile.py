from faker import Faker
from locust import HttpUser, task, SequentialTaskSet, TaskSet, constant_throughput
import random
import re

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
        self.client.post(
            "/registration/",
            data={
                "username": fake.user_name() + str(random.randint(10, 9999)),
                "email": fake.email(domain="mpt.ru"),
                "password1": password,
                "password2": password,
                "csrfmiddlewaretoken": token,
            },
            headers={"X-CSRFToken": token},
        )

class LoginAndBuy(SequentialTaskSet):

    @task
    def login(self):
        page = self.client.get("/login/")
        token = page.cookies.get("csrftoken")
        self.client.post(
            "/login/",
            data={
                "username": "admin",
                "password": "masha001",
                "csrfmiddlewaretoken": token,
            },
            headers={"X-CSRFToken": token, "Referer": f"{self.user.host}/login/"},
        )

    @task
    def open_products(self):
        response = self.client.get("/products/")
        ids = re.findall(r"/products/(\d+)/", response.text or "")
        self.product_id = ids[0] if ids else "1"

    @task
    def add_to_basket(self):
        product_id = getattr(self, "product_id", "1")
        detail = self.client.get(f"/products/{product_id}/")
        token = detail.cookies.get("csrftoken")
        self.client.post(
            f"/basket/add/{product_id}/",
            data={
                "count": random.randint(1, 3),
                "reload": False,
                "csrfmiddlewaretoken": token,
            },
            headers={
                "X-CSRFToken": token,
                "Referer": f"{self.user.host}/products/{product_id}/",
            },
        )

    @task
    def open_basket(self):
        self.client.get("/basket/")
        self.interrupt()


class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = constant_throughput(2)
    tasks = {
        SiteTests: 5,
        LoginAndBuy: 1,
    }
