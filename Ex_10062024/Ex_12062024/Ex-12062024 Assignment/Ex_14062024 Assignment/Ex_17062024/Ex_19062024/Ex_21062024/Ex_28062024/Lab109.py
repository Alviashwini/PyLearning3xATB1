class Myclass:

    def __init__(self):
        self.name = "Amit"
        self._email = "amit@gmail.com"
    def public_func(self):
        print("Public Func()")

    def __private_func(self):
        print("you can access me only via another method, this is private")

    def public_fn_private(self):
        self.__private_func()
        print(self._email)


# security : not everyone can access ur variables/methods
a = Myclass()
a.public_func()
a.public_fn_private()
