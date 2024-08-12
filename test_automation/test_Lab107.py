# How to add request module to project
import pytest
import allure
import requests
@allure.title("Test GET Request - RESTFUL Booker project#1")
@allure.description("TC#1 -> verify that GET Request with ID works")
@allure.tag("regression", "p0", "Smoke")
@allure.label("owner", "Ashwini")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200
@allure.title("Test GET Request - RESTFUL Booker project#1")
@allure.description("TC#2 -> verify that GET Request with invalid bookingID")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404

@allure.title("Test GET Request - RESTFUL Booker project#1")
@allure.description("TC#3 -> verify that GET Request with invalid booking ID")
@pytest.mark.smoke
def test_get_single_request_by_id_negative2():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404