
# Create invalid booking id with wrong payload
import pytest
import allure
import requests


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


def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    post_url = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "",
        "lastname": "",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Lunch"
    }
    response = requests.post(url=post_url, headers=headers, json=json_payload)

    assert response.status_code == 400
    #assert 'error' in response.json()
    #booking_id = data["bookingid"]
    # assert ["bookingid"] == "bookingid"
    # print(booking_id)
    # return booking_id

