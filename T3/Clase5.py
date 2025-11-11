# function  =  a block of reusable code 
#               place () after the fucction name to call it

def say_hi(name,lenguage):
    print(f"Hello {name}") 
    print(f"Welcome to {lenguage} Programming")

say_hi("Alice", "Python")

# default arguments

def say_hello(name, language="Python"):
    print(f"Hello {name}") 
    print(f"Welcome to {language} Programming")

say_hello("Bob")
say_hello("Charlie", "JavaScript")

# keyword arguments
def greet_user(name, greeting):
    print(f"{greeting}, {name}!")

greet_user(greeting="Good morning", name="Diana")

#*args = allows you to pass multiple non-key arguments to a function
# **kwargs  = allows you to pass multiple keyword arguments to a function
#     *unpacking operator
#    1.positional 2.default 3.keyword  4. arbitrary 


# no sabemos cuantos argumentos vamos a recibir
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total 

def multiply(*nums):
    total = 1
    for num in nums:
        total *= num
    return total


print(add(1))
print(multiply(2,3,4,5))

# usamos **kwargs para recibir argumentos con clave y valor

def print_address(**kwargs):
    #print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(name="Eve", city="Wonderland", country="Fiction")
print_address(street="123 Main St", zip="12345")

# aqui el orden importa primero los args y luego los kwargs 
def shipping_label(*args, **kwargs):
    print("Shipping to:")
    for arg in args:
        print(arg)
    print("Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

shipping_label("John Doe", "456 Elm St", city="Metropolis", country="Utopia", zip="67890")