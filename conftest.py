import pytest
import requests
from config import BASE_URL, USERNAME, PASS


@pytest.fixture(scope="session")
def auth_token():
    payload = {"username": USERNAME, "password": PASS}
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    token = response.json().get("token")
    return token


@pytest.fixture
def create_booking(auth_token):
    payload = {
        "firstname": "Yana",
        "lastname": "O",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-05"},
        "additionalneeds": "Wi-Fi"
    }
    response = requests.post(f"{BASE_URL}/booking", json=payload)
    booking_id = response.json()["bookingid"]
    yield booking_id
    url = f"{BASE_URL}/booking/{booking_id}"
    headers = {"Cookie": f"token={auth_token}"}
    requests.delete(url, headers=headers)
    print(f"\n[Cleanup] Booking {booking_id} deleted")
