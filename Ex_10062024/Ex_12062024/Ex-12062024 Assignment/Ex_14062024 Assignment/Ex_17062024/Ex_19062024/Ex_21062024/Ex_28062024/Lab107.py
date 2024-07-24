# Encapsulation
# Binding the data variables with the methods.
# DAta member/class variables
# methods (which are created) def - function within the class
# Wrapping/binding the data variables with the methods is Encapsulation
# Hide the data members( also known as class variables, instance variables) by using only methods

class car:
    name = None
    password = "123"

    def __init__(self):
        print("Iam caled when a object is created")
     # this is end of class
    def change_password(self):
        self.password = "345"

XUV = car()
XUV.password = "345"
# it means we need to change password by creating a function after constructor
