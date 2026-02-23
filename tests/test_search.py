import requests
from config import BASE_URL


def test_search_bookings_with_name(create_booking):
    url = f"{BASE_URL}/booking/"
    params = {
        "firstname": "Yana"
    }
    response = requests.get(url, params=params)
    assert response.status_code == 200
    bookings = response.json()
    assert len(bookings) > 0
    assert isinstance(bookings, list)
    assert "bookingid" in bookings[0]


def test_search_bookings_between_dates(create_booking):
    url = f"{BASE_URL}/booking/"
    params = {
        "checkin": "2025-12-01",
        "checkout": "2026-02-01"
    }
    response = requests.get(url, params=params)
    assert response.status_code == 200
    bookings = response.json()
    assert len(bookings) > 0
    assert isinstance(bookings, list)
    assert "bookingid" in bookings[0]
