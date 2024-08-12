import requests
import pytest
import allure
import openpyxl
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.utils.utils import Utils
from src.helpers.api_request_wrappers import *
from src.helpers.common_verifications import *


# Configuration file code which requires most of the time

# Create token and # Create booking id
@pytest.fixture(scope="session")
def create_token():
    # base_url = "https://restful-booker.herokuapp.com"
    # base_path = "/auth"
    # post_url = base_url + base_path
    # headers = headers = {"Content-Type": "application/json"}
    # json_payload = {
    #     "username": "admin",
    #     "password": "password123"
    # }
    # response = requests.post(url=post_url, headers=headers, json=json_payload)
    response = post_request(
        url=APIConstants().url_create_token(),
        headers=Utils().common_headers_json(),
        payload=payload_create_token(),
        auth=None,
        in_json=False
    )
    # assert response.status_code == 200
    # token = response.json()["token"]
    # print(token)
    # return token
    #token = response.json()["Token"]
    verify_http_status_code(response_data=response, expected_data=200)
    token = response.json()["token"]
    print(token)
    return token


@pytest.fixture(scope="session")
def create_booking():
    response = post_request(
        url=APIConstants().url_create_booking(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_booking(),
        in_json=False
    )
    verify_http_status_code(response_data=response, expected_data=200)
    booking_id = response.json()["bookingid"]
    print(booking_id)
    return booking_id
