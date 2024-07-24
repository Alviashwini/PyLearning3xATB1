# different types of functions are used
def talk(self):  # No argument no return type
    print("I can talk")


def sleep(self, name):  # Argument with No return type
    print("Iam a method")
    print("sleep", name)


def sleep2(self, name):  # Argument with return type
    print("iam a method")
    return None


def walk(self):
    print("Iam walking")


def walk_return(self):    # No Argument with return type
    return "Iam walking"
