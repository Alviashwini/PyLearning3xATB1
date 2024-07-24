# Web automation selenium real time ex how classes are used
# page you are going automate

class VWOloginpage:
    email = None
    password = None

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "pass123":
            print("Allowed to enter")
        else:
            print("Not Allowed to enter")

amit = VWOloginpage("amit@gmail.com", "123")
amit.login_confirm()

Ashwini = VWOloginpage("Ashwini@gmail.com", "pass123")
Ashwini.login_confirm()
