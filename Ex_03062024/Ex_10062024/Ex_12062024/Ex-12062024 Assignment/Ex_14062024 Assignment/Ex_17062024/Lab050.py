# f1 function
def f1(a, b, c):
    return a + b + c

print("Hello")
print("hello") # if print is typed in middle of this line means outside the function it will not be executed.

def f1(a, b, c):
    return a + b + c

result = f1(5,5,6)
print(result)
# another way
result = f1(a=10, b=3, c=2)
print(result)
# or
print(f1(1,2,3))
