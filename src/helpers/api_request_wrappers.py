import requests
import json


def get_request(url, auth):
    response = requests.get(url=url, auth=auth)
    return response.json()


def post_request(url, headers, payload, auth, in_json):
    response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response


def put_request(url, headers, payload, auth, in_json):
    response = requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response


def patch_request(url, headers, payload, auth, in_json):
    response = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response


def delete_request(url, headers, payload, auth, in_json):
    response = requests.delete(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response
