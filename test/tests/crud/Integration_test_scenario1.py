# 1.Verify create booking --> patch request -->verify the firstname  is updated
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


def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    post_url = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Abhishek",
        "lastname": "Rawat",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Lunch"
    }
    response = requests.post(url=post_url, headers=headers, json=json_payload)

    assert response.status_code == 200
    data = response.json()
    booking_id = data["bookingid"]
    #assert ["bookingid"] == "bookingid"
    return booking_id


@allure.title("Verify by updating firstname")
@allure.description("Verify by creating a booking id and also verify by updating firstname using patch method")
def test_patch_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    patch_url = base_url + base_path
    cookie = "token=" + create_token()
    headers = {"Content-Type": "application/json",
               "Cookie": cookie}
    json_payload = {
        "firstname": "Ashish",
    }
    response = requests.patch(url=patch_url,headers=headers,json=json_payload)
    assert response.status_code == 200
    firstname = response.json()
    print(firstname)
