# oops concept
# important interview question
class person:
    # class variables/instance variables
    name = "Ashwini"
    age = "None"

    def walk(self):
        a = 10  # local variable
        print("Iam a method")
        print("Hi", self.age)


Ashwini = person()
Ashwini.walk()
