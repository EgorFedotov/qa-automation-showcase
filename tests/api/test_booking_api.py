"""REST API tests against the restful-booker sandbox.

Covers auth, full CRUD and negative checks — the everyday backend QA loop.
"""
import allure
import pytest

pytestmark = pytest.mark.api


@allure.feature("Booking API")
@allure.story("Auth")
def test_auth_returns_token(auth_token):
    assert isinstance(auth_token, str) and len(auth_token) > 0


@allure.feature("Booking API")
@allure.story("Read")
def test_get_all_bookings_returns_list(session, api_url):
    resp = session.get(f"{api_url}/booking", timeout=15)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert all("bookingid" in item for item in data)


@allure.feature("Booking API")
@allure.story("Create")
def test_create_booking(session, api_url, booking_data):
    resp = session.post(f"{api_url}/booking", json=booking_data, timeout=15)
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert isinstance(body["bookingid"], int)
    assert body["booking"]["firstname"] == booking_data["firstname"]
    assert body["booking"]["totalprice"] == booking_data["totalprice"]


@allure.feature("Booking API")
@allure.story("Read")
def test_get_booking_by_id(session, api_url, new_booking):
    booking_id, payload = new_booking
    resp = session.get(f"{api_url}/booking/{booking_id}", timeout=15)
    assert resp.status_code == 200
    body = resp.json()
    assert body["firstname"] == payload["firstname"]
    assert body["lastname"] == payload["lastname"]


@allure.feature("Booking API")
@allure.story("Update")
def test_full_update_requires_auth(session, api_url, new_booking, auth_token):
    booking_id, _ = new_booking
    updated = {
        "firstname": "Updated",
        "lastname": "Name",
        "totalprice": 999,
        "depositpaid": False,
        "bookingdates": {"checkin": "2026-08-01", "checkout": "2026-08-05"},
        "additionalneeds": "Late checkout",
    }
    resp = session.put(
        f"{api_url}/booking/{booking_id}",
        json=updated,
        headers={"Cookie": f"token={auth_token}"},
        timeout=15,
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["firstname"] == "Updated"
    assert body["totalprice"] == 999


@allure.feature("Booking API")
@allure.story("Update")
def test_partial_update_booking(session, api_url, new_booking, auth_token):
    booking_id, _ = new_booking
    resp = session.patch(
        f"{api_url}/booking/{booking_id}",
        json={"firstname": "Patched"},
        headers={"Cookie": f"token={auth_token}"},
        timeout=15,
    )
    assert resp.status_code == 200, resp.text
    assert resp.json()["firstname"] == "Patched"


@allure.feature("Booking API")
@allure.story("Delete")
def test_delete_booking_removes_it(session, api_url, booking_data, auth_token):
    created = session.post(f"{api_url}/booking", json=booking_data, timeout=15)
    booking_id = created.json()["bookingid"]

    resp = session.delete(
        f"{api_url}/booking/{booking_id}",
        headers={"Cookie": f"token={auth_token}"},
        timeout=15,
    )
    assert resp.status_code in (200, 201), resp.text

    check = session.get(f"{api_url}/booking/{booking_id}", timeout=15)
    assert check.status_code == 404
