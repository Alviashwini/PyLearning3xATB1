# lab 105 class loginpage using input function method
class VWOloginpage():
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "pass123":
            print("Allowed to enter")
        else:
            print("Not Allowed to enter")


email = input("Enter the email \n")
password = input("Enter the password \n")
amit = VWOloginpage(email, password)
amit.login_confirm()

Ashwini = VWOloginpage(email, password)
Ashwini.login_confirm()
