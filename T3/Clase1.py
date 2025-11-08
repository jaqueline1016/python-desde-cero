# while loop  =  execute some code while some condition remains true 

age  =  int(input("Enter your age:"))

while age < 0:
    print("Age can't be nagative")
    age  =  int(input("Enter your age:"))

print(f"Your are {age} years old")


#  for loops  =  execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

for x in range(1,11):
    print(x)

for x in reversed(range(1,11)):
    print(x)

for x in range(1,11,2):
    print(x)

for x in range(1,21):
    if x == 13:
        continue
    else:
        break
    
print("bye")