import requests
import pytest
import allure
import openpyxl
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.utils.utils import Utils
from src.helpers.api_request_wrappers import *
from src.helpers.common_verifications import *


# Create token function
#@pytest.fixture(scope="session")
def test_create_token():
    response = post_request(
        url=APIConstants().url_create_token(),
        headers=Utils().common_headers_json(),
        payload=payload_create_token(),
        auth=None,
        in_json=False
    )
    #response = response.json()
    verify_http_status_code(response_data=response, expected_data=200)
    token = response.json()["token"]
    print(token)
    return token


def test_create_booking():
    response = post_request(
        url=APIConstants().url_create_booking(),
        headers=Utils().common_headers_json(),
        payload=payload_create_booking(),
        auth=None,
        in_json=False
    )

    verify_http_status_code(response_data=response, expected_data=200)
    booking_id = response.json()["bookingid"]
    print(booking_id)
    return booking_id
