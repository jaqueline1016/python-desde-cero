# index =  [start :  end : step ]

credicard_number = "1234-5678-9012-3456"

credictard_slice = credicard_number[0:4]  # '1234'
reverso =  credicard_number[::-1]  # '6543-2109-8765-4321'
print(reverso)
print(credictard_slice)


# {value.flags}  format  

price1 =  3.4587996
price2 =  -987.47
price3 =  12.34

print(f"Price 1  is {price1}")
print(f"Price 2 is {price2}")
print(f"Price 3 is {price3}")
print("-------------")
print(f"Price 1  is {price1: .3f}")
print(f"Price 2 is {price2:.3f}")
print(f"Price 3 is {price3:.3f}")
print("-------------")
print(f"Price 1  is {price1:10}")
print(f"Price 2 is {price2:010}")
print(f"Price 3 is {price3:10}")
print("-------------")
print(f"Price 1  is {price1:<10}")
print(f"Price 2 is {price2:>10}")
print(f"Price 3 is {price3:^10}")
print("-------------")
print(f"Price 1  is {price1:+}")
print(f"Price 2 is {price2:+}")
print(f"Price 3 is {price3: }")
print("-------------")
print(f"Price 1  is {price1:,}")
print(f"Price 2 is {price2:,.2f}")
print(f"Price 3 is {price3:+,.2f}")