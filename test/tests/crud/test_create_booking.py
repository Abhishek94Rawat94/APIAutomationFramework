import pytest
import allure
import json
from src.constants.api_constants import *
from src.utils.utils import *
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
from src.helpers.api_request_wrappers import *


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify test create booking status and booking id shouldn't be null")
    @allure.description("Create a booking from payload and "
                        "verify that booking id should not be null and status code should be 200")
    def test_create_booking_positive(self):
        response = post_request(url=APIConstants().url_create_booking(),
                                headers=Utils().common_headers_json(),
                                auth=None,
                                payload=payload_create_booking(),
                                in_json=False)

        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response, expected_data=200)
        verify_json_key_not_null(response.json()["bookingid"])
        print(f'Booking id is {booking_id}')

    @pytest.mark.negative
    @allure.title("Negative test case for create booking")
    @allure.description(
        "Booking should not get created with empty payload and also check the response code should be 500")
    def test_create_booking_negative(self):
        response = post_request(url=APIConstants().url_create_booking(),
                                headers=Utils().common_headers_json(),
                                auth=None,
                                payload={},
                                in_json=False)
        #update_response = response.json()
        verify_http_status_code(response_data=response, expected_data=500)
        #print(f"Update Response Body: {update_response.text}")

    @pytest.mark.negative
    @allure.title("Verify booking should not get created with negative price")
    @allure.description("Booking should not be created if total price of booking is -50")
    def test_create_booking_negative2(self):
        response = post_request(url=APIConstants().url_create_booking(),
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload={
                                    "firstname": "Amity",
                                    "lastname": "Brown",
                                    "totalprice": -50,
                                    "depositpaid": True,
                                    "bookingdates": {
                                        "checkin": "2018-01-01",
                                        "checkout": "2019-01-01"
                                    },
                                    "additionalneeds": "Breakfast"
                                },
                                in_json=False
                                )

        verify_http_status_code(response_data=response, expected_data=400)
        print(response.json())

    @pytest.mark.negative
    @allure.title("Verify booking should not get created with invalid first name")
    @allure.description("Booking should not be created with invalid firstname by giving special character in firstname Abhi@321")
    def test_spc_char_in_firstname_negative3(self):
            response = post_request(url=APIConstants().url_create_booking(),
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload={
                                    "firstname": "Abhi@321",
                                    "lastname": "Brown",
                                    "totalprice": 500,
                                    "depositpaid": True,
                                    "bookingdates": {
                                        "checkin": "2018-01-01",
                                        "checkout": "2019-01-01"
                                    },
                                    "additionalneeds": "Breakfast"
                                },
                                in_json=False
                                )

            verify_http_status_code(response_data=response,expected_data=400)

    @pytest.mark.negative
    @allure.title("Verify booking should not get created with missing data")
    @allure.description(
        "Booking should not be created with missing data in firstname and lastname")
    def test_negative4(self):
        response = post_request(url=APIConstants().url_create_booking(),
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload={
                                    "firstname": "",
                                    "lastname": "",
                                    "totalprice": 500,
                                    "depositpaid": True,
                                    "bookingdates": {
                                        "checkin": "2018-01-01",
                                        "checkout": "2019-01-01"
                                    },
                                    "additionalneeds": "Breakfast"
                                },
                                in_json=False
                                )

        verify_http_status_code(response_data=response, expected_data=400)

    @pytest.mark.negative
    @allure.title("Verify booking should not get created with wrong url")
    @allure.description("Verify the booking should not get created if the url wrong ur is provided")
    def test_negative5(self):
        response = post_request(url="https://restful-booker.herokuapp.com/ticketing",
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False
                                )

        verify_http_status_code(response_data=response,expected_data=404)

