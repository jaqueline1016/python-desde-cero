# Weight converter

weight =  float(input("Enter your weight : "))
unit =  input("Enter the unit (kg or lb): ")    

if unit.lower() == "kg":
    converted_weight = weight * 2.20462
    print(f"Weight in pounds: {round(converted_weight, 2)} lb")
elif unit.lower() == "lb":
    converted_weight = weight / 2.20462
    print(f"Weight in kilograms: {round(converted_weight, 2)} kg")
else:
    print("Invalid unit. Please enter 'kg' or 'lb'.")
