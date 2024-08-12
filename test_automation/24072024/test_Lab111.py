# for put request we need url, path param- in pp we need to chk booking id exists or not,
# token-Auth
# payload

import allure
import pytest
import requests

def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token
def create_booking():
    print("Create Booking Testcase")
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
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
    response = requests.post(url=url, headers=headers, json=json_payload)
    print(type(url))
    print(type(headers))
    print(type(json_payload))
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id
def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    PUT_URL = base_url + base_path

    cookie = "token" + create_token()
    headers = {
        "Content-Type": "application/json",
        "cookie": cookie
    }
    json_payload = {
        "firstname": "Ashwini",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 403
    data = response.json()
    assert data["firstname"] == "Ashwini"

def test_delete():
    url = "https://restful-booker.herokuapp.com/booking"
    booking_id = create_booking()
    DELETE_URL = url + str(booking_id)
    cookie_value = "token" + create_token()
    headers = {
        "Content-Type": "application/json",
        "cookie": cookie_value
    }
    print(headers)



