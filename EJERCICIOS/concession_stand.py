menu = {
    "Hot Dog": 2.50,
    "Burger": 3.00,
    "Fries": 1.50,
    "Soda": 1.00,
    "Candy": 0.75,
    "Pizza": 4.00,
    "Ice Cream": 2.25,
    "Popcorn": 1.75,
}

cart = []
total  = 0

print("Welcome to the Concession Stand!")
print("Here is our menu:")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-" * 30)

while True:
    food =  input("Select an item (q to quit): ")
    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-" * 30)
print("You Order: ")      
for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"\nYour total is: ${total:.2f}")


