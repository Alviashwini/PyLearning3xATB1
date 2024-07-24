class VWOLogin:

    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def login_confirm(self):
        if self.__email == "abc@gmail.com" and self.__password == "123":
            print("Allowed")
        else:
            print("Not Allowed")

page1 = VWOLogin("abc@gmail.com", "123")
page1.login_confirm()
# below are private
# page1.__email == "??"
# page1.__password == "??"
