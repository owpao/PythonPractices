# Write a Python program which accepts the radius of a circle from the user and compute the area

# area of a circle
# area = pi(r)^2

import math

radius = float(input("Enter the radius of your circle: "))
area = float(math.pi*radius*radius)

print("The area of the circle is:", area)