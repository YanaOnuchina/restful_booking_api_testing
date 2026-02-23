import requests
import pytest
from jsonschema import validate

from config import BASE_URL


def test_create_booking():
    payload = {
        "firstname": "Yana",
        "lastname": "O",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-05"},
        "additionalneeds": "Wi-Fi"
    }
    response = requests.post(f"{BASE_URL}/booking", json=payload)
    assert response.status_code == 200
    assert response.json().get("booking") == payload


def test_delete_booking(auth_token, create_booking):
    url = f"{BASE_URL}/booking/{create_booking}"
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 201  # special code in Restful-booking API
    # Check booking was deleted
    response = requests.get(url)
    assert response.status_code == 404


def test_get_all_bookings():
    url = f"{BASE_URL}/booking/"
    response = requests.get(url)
    assert response.status_code == 200
    assert len(response.json()) > 0
    print(f"\nBookings number: {len(response.json())}")


def test_get_booking(create_booking):
    url = f"{BASE_URL}/booking/{create_booking}"
    response = requests.get(url)
    schema = {
        "type": "object",
        "properties": {
            "firstname": {"type": "string"},
            "lastname": {"type": "string"},
            "totalprice": {"type": "number"},
            "depositpaid": {"type": "boolean"},
            "bookingdates": {
                "type": "object",
                "properties": {
                    "checkin": {"type": "string"},
                    "checkout": {"type": "string"}
                },
                "required": ["checkin", "checkout"]
            },
            "additionalneeds": {"type": "string"}
        },
        "required": ["firstname", "lastname", "totalprice"]
    }
    assert response.status_code == 200
    validate(response.json(), schema=schema)


def test_booking_full_update(auth_token, create_booking):
    url = f"{BASE_URL}/booking/{create_booking}"
    payload = {
        "firstname": "Noname",
        "lastname": "Guest",
        "totalprice": 300,
        "depositpaid": False,
        "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-07"},
        "additionalneeds": "Wi-Fi"
    }
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == payload


def test_booking_partial_update(auth_token, create_booking):
    new_price = 300
    url = f"{BASE_URL}/booking/{create_booking}"
    headers = {"Cookie": f"token={auth_token}"}
    payload = {"totalprice": new_price}
    response = requests.patch(url, json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json().get("totalprice") == new_price
