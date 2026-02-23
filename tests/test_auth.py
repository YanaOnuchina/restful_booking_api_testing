import requests
from config import USERNAME, PASS, BASE_URL


def test_correct_auth():
    payload = {"username": USERNAME, "password": PASS}
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    assert response.status_code == 200
    assert "token" in response.json(), f"Token not found in response: {response.text}"


def test_bad_pass():
    payload = {"username": USERNAME, "password": ""}
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    assert response.status_code == 200  # special feature of Restful-booking API
    assert response.json().get("reason") == "Bad credentials"


def test_bad_username():
    payload = {"username": "", "password": PASS}
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    assert response.status_code == 200  # special feature of Restful-booking API
    assert response.json().get("reason") == "Bad credentials"
