#  Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24
factorial = int(input("Enter the Number:\n"))
num = 1
for i in range(1, factorial+1):
    num = num*i
print(f"The Factorial of {factorial} is {num}")