# creating class calc using constructor
class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


print(Calc(3,4).sum())
print(Calc(3,4).div())
print(Calc(3,4).mul())
