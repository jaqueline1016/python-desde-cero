# logical opertaors
# or  =  at least one condition is true
# and =  both conditions are true
# not =  reverses the result, false becomes true and true becomes false

temp =  15
is_summer =  True

if temp > 30 and is_summer:
    print("It's hot outside!")
elif temp <= 20 or  is_summer:
    print("It's a warm summer day.")
elif not is_summer:
    print("It's not summer.")
else:
    print("It's a cool day.")
