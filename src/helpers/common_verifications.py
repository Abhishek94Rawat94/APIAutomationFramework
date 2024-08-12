def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Expected code is Not same"


def verify_the_json_response(response_data, expected_data):
    assert response_data == expected_data


def verify_json_key_not_null(key):
    assert key != 0, "Key is non empty" + key
    assert key > 0, "Key is greater than 0"


def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed-Key is non empty" + key


def verify_response_key_should_be_not_none(key):
    assert key is not None
