# 6. Trying to Update on a Delete ID -> 404

import allure
import pytest
import requests

@pytest.fixture()
def create_token():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/auth"
    post_url = base_url + base_path
    headers = headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=post_url, headers=headers, json=json_payload)
    assert response.status_code == 200
    token = response.json()["token"]
    print(token)
    return token

@pytest.fixture()
@allure.title("Create a new booking")
def create_booking():
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    data = response.json()
    booking_id = data["bookingid"]
    print(f"Created Booking ID: {booking_id}")
    return booking_id


@allure.title("#TC6 - Trying to update a deleted booking ID")
@pytest.mark.integration
def test_update_deleted_booking(create_token, create_booking):
    booking_id = create_booking
    base_url = "https://restful-booker.herokuapp.com/booking/"
    DELETE_URL = base_url + str(booking_id)

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    # Delete the booking
    delete_response = requests.delete(url=DELETE_URL, headers=headers)
    assert delete_response.status_code == 201
    print(f"Deleted Booking ID: {booking_id}")

    # Try to update the deleted booking
    UPDATE_URL = DELETE_URL

    update_payload = {
        "firstname": "Vimal",
        "lastname": "Patel",
    }

    update_response = requests.patch(url=UPDATE_URL, headers=headers, json=update_payload)
    assert update_response.status_code == 405
    assert "text/plain" in update_response.headers["Content-Type"]
    print(f"Update Response Status Code: {update_response.status_code}")
    print(f"Update Response Body: {update_response.text}")