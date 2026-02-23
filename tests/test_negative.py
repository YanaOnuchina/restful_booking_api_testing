import requests
from config import BASE_URL


def test_create_empty_booking():
    response = requests.post(f"{BASE_URL}/booking", json={})
    assert response.status_code == 500  # According API documentation


def test_delete_unavailable_booking(auth_token):
    invalid_id = 99999999
    url = f"{BASE_URL}/booking/{invalid_id}"
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 405  # According API documentation


def test_booking_unauthorized_update(create_booking):
    url = f"{BASE_URL}/booking/{create_booking}"
    payload = {
        "firstname": "Noname",
        "lastname": "Guest",
        "totalprice": 300,
        "depositpaid": False,
        "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-07"},
        "additionalneeds": "Wi-Fi"
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 403
