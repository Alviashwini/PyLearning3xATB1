# Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than, or equal to the second number.
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))


def compare_numbers(num1, num2):
    if num1 > num2:
        return "The first number is greater than the second number."
    elif num1 < num2:
        return "The first number is less than the second number."
    else:
        return "The fist number is equal to the second number."
    num1 = float(input("Enter the first number:  "))
    num2 = float(input("Enter the second number: "))
    result = compare_numbers(num1, num2)
    print(result)


print(f"{num1} is {'greater than' if num1 > num2 else 'less than' if num1 < num2 else 'equal to'} {num2}.")
