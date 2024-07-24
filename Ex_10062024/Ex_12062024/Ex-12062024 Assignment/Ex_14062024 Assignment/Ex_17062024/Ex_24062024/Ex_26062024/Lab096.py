# Ex of class
class person:
    # Attributes
    name = None
    id = None
    age = None
    Phone_number = None

    # we are writing none bcz there is no value.

    # Behaviour is created by using function
    def talk(self):
        print("I can talk")

    def walk(self):
        print("iam walking")


# create object of the person class\
# object reference = object -> className()
Ashwini = person()
Ashwini.name = "Ashwini peteti"
Ashwini.talk()

Praveen = person()
Praveen.name = "Praveen peteti"
Praveen.walk()
# above line . (dot) is used to access the object
