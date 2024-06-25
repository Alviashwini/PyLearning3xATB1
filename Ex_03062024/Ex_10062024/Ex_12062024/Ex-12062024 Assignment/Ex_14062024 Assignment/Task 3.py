#  Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24
factorial = int(input("Enter the Number:\n"))
num = 1
for i in range(1, factorial + 1):
    num = num * i
print(f"The Factorial of {factorial} is {num}")
# or
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(factorial)
# or we can use while loop also
n = 5
factorial = 1
while n > 0:
    factorial = factorial * n
    n = n - 1

print(factorial)


