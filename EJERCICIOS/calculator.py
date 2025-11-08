# Calculator 

opertator =  input("Enter operator (+, -, *, /): ")
num1 =  float(input("Enter first number: "))
num2 =  float(input("Enter second number: "))

if opertator == "+":
    result = num1 + num2
    print(round(result,3))
elif opertator == "-":
    result = num1 - num2
    print(round(result,3))
elif opertator == "*":
    result = num1 * num2
    print(round(result,3))
elif opertator == "/":
    result = num1 / num2
    print(round(result,3))
else:
    print(f"Invalid operator: {opertator}")
    

