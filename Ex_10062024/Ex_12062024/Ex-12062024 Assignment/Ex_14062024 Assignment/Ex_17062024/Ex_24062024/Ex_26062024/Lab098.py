# constructor is used to initialize values of instance variables(Attributes)
class Dog:
    name = None

    def sleep(self):
        print("sleeping")


Dog1 = Dog()
print(Dog1.name)
Dog1.name = "chow"
print(Dog1.name)
Dog1.sleep()

print("- ______________________")
dog2 = Dog()
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)
# Instead of above while creating the object we can set the function means value of name.
# line 8 & 15
# function is below
def _init_(self, name, id):    # self, name, id are arguments
    self.name = name
    self.id = id
# continued in next