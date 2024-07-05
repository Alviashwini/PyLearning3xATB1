# Leetcode example means sum of digits

number = 12345
r1 = number % 10
q1 = number // 10
print(r1)
print(q1)

r2 = q1 % 10
q2 = q1 // 10
print(r2)
print(q2)

r3 = q2 % 10
q3 = q2 // 10
print(r3)
print(q3)

r4 = q3 % 10
q4 = q3 // 10
print(r4)
print(q4)

r5 = q4 % 10
q5 = q4 // 10
print(r5)
print(q5)

print(r1 + r2 + r3 + r4 + r5)


# above one using recursive function
# /  means division
# //  means quotient
# % means Remainder
def sum_of_digits(n):
    # Base case
    if n < 10:
        return n
    # recursive case
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(12345))
