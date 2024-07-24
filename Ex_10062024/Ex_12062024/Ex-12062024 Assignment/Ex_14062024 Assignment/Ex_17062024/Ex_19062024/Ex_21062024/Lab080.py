# Decorator is essentially a function that takes another function as an argument
# and return new function that extends the behavior
# for ex: if we want to say hello we will write def say_hello():
# it will not print anything to decorate this we will use
def my_decorator(func):
    def wrapper():
        print("starting......")
        print("***********")
        func()
        print("**********")
        print("Ending")

    return wrapper()

@my_decorator
def func():
        print("say_hello")






