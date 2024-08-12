# .env file is used to store important info like passwords,credentials in framework.

from dotenv import load_dotenv
import os
def test_update_req():
    load_dotenv()
    url = os.getenv("URL")
    print(url)
    username = os.getenv("USERNAME")
    print(username)
    password = os.getenv("PASSWORD")
    print(password)