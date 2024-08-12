
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


def create_booking_id():
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

def test_update_req_1(create_token,create_booking_id):
    print("Token->", create_token)
    print("Booking ID->", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com/booking/" + create_booking_id
    cookie = "token=" + create_token
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

    response = requests.put(url=base_url, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "Ashwini"

def test_update_req_2(create_token, create_booking_id):
    print("Token->", create_token)
    print("Booking ID->", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com/booking/" + create_booking_id
    cookie = "token=" + create_token
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

    response = requests.put(url=base_url, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "Ashwini"






