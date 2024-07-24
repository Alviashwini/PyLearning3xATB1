class Calc:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object_ref = Calc()
output = object_ref.sum(3,4)
print(output)
output = object_ref.sub(6,4)
print(output)
output = object_ref.div(5,3)
print(output)
output = object_ref.mul(3,4)
print(output)