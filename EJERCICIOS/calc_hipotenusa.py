# Calculo de la hipotenusa de un triángulo rectángulo
import math

a  = float(input("Enter side a: "))
b =  float(input("Enter side b: "))

c  =  math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse is: {round(c,2)}")
