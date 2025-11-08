# calculate the radius of a circle 

import math

radius = float(input("Enter the radius of the circle: "))



area = math.pi * pow(radius, 2)

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference,2)}cm")
print(f"The area is: {round(area,2)}cm²")


