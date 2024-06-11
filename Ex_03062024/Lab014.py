# Take the int 2 numbers from the user and we want to add them
# We need to use the input() function
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result = num1+num2
print(result)
# In this case means line 5 result is concatenation so we have to use type conversion
# type conversion - string -> int -> ? int()
result = int(num1) + int(num2)
print(result)
print(type(int(num1)))



