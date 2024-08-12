import requests

def test_selenium(launch_Browser, close_Browser):
    launch_Browser
    print("Do something")
    close_Browser

