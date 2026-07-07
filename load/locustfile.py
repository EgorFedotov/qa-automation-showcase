"""Load test against the restful-booker sandbox.

Interactive UI:
    locust -f load/locustfile.py --host https://restful-booker.herokuapp.com

Headless (20 users, 1 minute):
    locust -f load/locustfile.py --host https://restful-booker.herokuapp.com \
        --users 20 --spawn-rate 5 --run-time 1m --headless
"""
from locust import HttpUser, between, task


class BookingApiUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def list_bookings(self):
        self.client.get("/booking", name="GET /booking")

    @task(2)
    def health_check(self):
        self.client.get("/ping", name="GET /ping")

    @task(1)
    def create_booking(self):
        self.client.post(
            "/booking",
            name="POST /booking",
            json={
                "firstname": "Load",
                "lastname": "Test",
                "totalprice": 100,
                "depositpaid": True,
                "bookingdates": {"checkin": "2026-07-10", "checkout": "2026-07-12"},
                "additionalneeds": "Breakfast",
            },
        )
