import pytest
import allure
import requests

@allure.title("Test GET Request - RESTFUL Booker project#1")
@allure.description("TC#4 -> verify that GET Request with ID works")
@allure.tag("regression", "p0", "Smoke")
@allure.label("owner", "Ashwini")
@allure.testcase("TC#4")

def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.text)
    print(responseData.headers)
    print(responseData.cookies)
    print(responseData.json())
    assert responseData.status_code == 200
