# To make request
# Url, method-POST,payload-(Data,body)
# headers- (content,type = Application/JSON),
# no auth required
import pytest
import allure
import requests


@allure.title("create booking CRUD")
@allure.description("TC#1 - verify the create booking")
@pytest.mark.crud
def test_create_booking_positive():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"content-Type:" "application/json"}
    payload = {
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

    response = requests.post(url, headers, payload)
    responseData = response.json()
    assert responseData.status_code == 200
    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] > 0
    assert type(responseData["bookingid"]) == int
    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]
    assert firstname == "jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True

    checkin = responseData["booking"]["booking dates"]["checkin"]
    checkout = responseData["booking"]["booking dates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"
