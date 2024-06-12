# Program calculate area of circle
# Data types
# input -->  radius --> int or float
# output --> area --> float
# core logic --> pi*r*r= 3.14
radius = float(input("Enter the radius\n"))
import math
print(math.pi)
area = math.pi * (radius ** 2)
print(area)

# Other way in one line
import math

print(math.pi * (float(input("Enter the radius\n")) ** 2))
