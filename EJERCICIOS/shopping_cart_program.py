# Shopping cart program

item  =  input("Enter the item you want to buy: ")
price =  float(input("waht is the price?:"))
quantity = int(input("How many do you want to buy?: "))
total =  price * quantity

print(f"You have added {quantity} {item}(s) to your cart. The total price is: ${total:.2f}")