# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# output is Leapyear
# input = 2024

year = int(input("Enter year:\n"))

if year%4 == 0 or year%400 == 0:
print("leap year")
elif year % 100 ! = 0:

    print("not a leap year")
else:
    print("invalid entry")
