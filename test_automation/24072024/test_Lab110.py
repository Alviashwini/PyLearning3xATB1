import pytest
import allure
import requests

@allure.title("create booking CRUD")
@allure.description("TC#2 - verify booking is not created with {} data")
@pytest.mark.crud
def test_create_booking_negative():
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"content-Type:" "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    responseData = response.json()
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    assert responseData.status_code == 500
@allure.title("create booking CRUD")
@allure.description("TC#3 - verify booking with totalprice string negative")
@pytest.mark.crud
def test_create_booking_negative():
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"content-Type:" "application/json"}
    json_payload = {
        "firstname": "sally",
        "lastname": "brown",
        "totalprice": "Ashwini",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    responseData = response.json()
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    assert responseData.status_code == 200
