# Convertidor de temperatura

unit  =  input("Ingrese la unidad de temperatura que desea convertir (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
temp =  float(input("Ingrese la temperatura que desea convertir: "))



if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print(f"{temp}°C son {fahrenheit}°F y {kelvin}K")
elif unit == "F":
    celsius = (temp - 32) * 5/9
    kelvin = (temp - 32) * 5/9 + 273.15
    print(f"{temp}°F son {celsius}°C y {kelvin}K")
elif unit == "K":
    celsius = temp - 273.15
    fahrenheit = (temp - 273.15) * 9/5 + 32
    print(f"{temp}K son {celsius}°C y {fahrenheit}°F")
else:
    print("Unidad no válida. Por favor, ingrese C, F o K.")


