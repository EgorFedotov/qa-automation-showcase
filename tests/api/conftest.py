"""Fixtures for the REST API test suite (restful-booker)."""
import pytest
import requests

from config import API_ADMIN_PASSWORD, API_ADMIN_USER, API_BASE_URL


@pytest.fixture(scope="session")
def api_url():
    return API_BASE_URL


@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json", "Accept": "application/json"})
    yield s
    s.close()


@pytest.fixture(autouse=True)
def api_available(session, api_url):
    """Skip API tests gracefully if the public sandbox is down (keeps CI green)."""
    try:
        resp = session.get(f"{api_url}/ping", timeout=10)
    except requests.RequestException as exc:
        pytest.skip(f"restful-booker sandbox unreachable: {exc}")
    if resp.status_code not in (200, 201):
        pytest.skip(f"restful-booker sandbox not healthy: {resp.status_code}")


@pytest.fixture(scope="session")
def auth_token(session, api_url):
    resp = session.post(
        f"{api_url}/auth",
        json={"username": API_ADMIN_USER, "password": API_ADMIN_PASSWORD},
        timeout=15,
    )
    assert resp.status_code == 200, resp.text
    token = resp.json().get("token")
    assert token, "No token returned by /auth"
    return token


def _booking_payload(**overrides):
    payload = {
        "firstname": "Egor",
        "lastname": "Fedotov",
        "totalprice": 145,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-07-10", "checkout": "2026-07-20"},
        "additionalneeds": "Breakfast",
    }
    payload.update(overrides)
    return payload


@pytest.fixture
def booking_data():
    return _booking_payload()


@pytest.fixture
def new_booking(session, api_url, auth_token):
    """Create a booking, yield (id, payload), then delete it in teardown."""
    payload = _booking_payload()
    resp = session.post(f"{api_url}/booking", json=payload, timeout=15)
    assert resp.status_code == 200, resp.text
    booking_id = resp.json()["bookingid"]
    yield booking_id, payload
    session.delete(
        f"{api_url}/booking/{booking_id}",
        headers={"Cookie": f"token={auth_token}"},
        timeout=15,
    )
