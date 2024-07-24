class car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected123"
        self.__private_var = "pass123"
        # this is end of class

    def __private_method(self):
        print("protected")

    def Printname(self):
        self.__private_method()
        if self.__private_var == "123":
            print("Hi, 123")
            print ("Iam allowed public")


alto = car()
alto.Printname()