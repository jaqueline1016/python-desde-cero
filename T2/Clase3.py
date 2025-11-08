# if =  a conditional statement used to execute a block of code if a specified condition is true.

age =  int(input("Enter your age: "))


if age >= 18:
    print("You are an adult.")  
else:
    print("You are a minor.")

# --------------------------------

response  =  input("Would you like food? (yes/no): ")

if response.lower() == "yes":
    print("Here is your food.")
else:
    print("No food for you.")

# --------------------------------

name =  input("Enter your name: ")

if name == "":
    print("You did not enter a name.")
else:
    print(f"Hello, {name}!")

# --------------------------------
for_sale =  True
 
if for_sale:
    print("This item is for sale.")
else: 
    print("This item is not for sale.")