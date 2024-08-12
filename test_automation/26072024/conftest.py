import pytest
import requests
@pytest.fixture()
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

@pytest.fixture()
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
    return str(data["bookingid"])

@pytest.fixture()
def read_csv_file_data():
    pass

@pytest.fixture()
def read_mysql_file_database():
    pass
@pytest.fixture()
def launch_Browser():
    print("Launching a Browser! chrome")
    return "chrome"

@pytest.fixture()
def close_Browser():
    print("closing a Browser! chrome")
    return "closed"

@pytest.fixture()
def read_url_testdata_Excel():
    pass

