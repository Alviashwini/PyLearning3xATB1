# important concept Recursion
# Recursion is a programming technique where a function calls itself inorder to solve a problem.
# key concepts
# Base case
# Recursive case
# for factorial

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))
