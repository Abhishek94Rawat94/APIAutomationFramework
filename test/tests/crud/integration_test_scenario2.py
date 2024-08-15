# Create a booking --> delete booking with id --> verify by get to check it does not exist.
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
        # assert ["bookingid"] == "bookingid"
        print(booking_id)
        return booking_id

def test_delete_booking():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking/"+str(create_booking())
    delete_url = base_url+base_path
    cookie = "token="+create_token()
    headers= {"Content-Type":"application/json",
              "Cookie":cookie}
    print(headers)
    response=requests.delete(url=delete_url,headers=headers)
    assert response.status_code==201

@allure.title("Get booking id")
@allure.description("To verify booking created and then deleted should not exist")
def test_get_booking():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking/"+str(create_booking())
    get_url=base_url+base_path
    response = requests.get(url=get_url)
    assert response.status_code==404
    # if response.status_code == 200:
    #     print("Booking exists:", response.json())
    #     return True
    #
    # elif response.status_code == 404:
    #     print("Booking not found.")
    #     return False
    #
    # else:
    #     print("Failed to get booking",response.json())
    #     return None