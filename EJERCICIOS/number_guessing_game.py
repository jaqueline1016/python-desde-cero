import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guess = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {lowest_num} and {highest_num}.")

while is_running:
    try:
        guess = int(input("Make a guess: "))
        
        if guess < lowest_num or guess > highest_num:
            print(f"Please guess a number within the range of {lowest_num} to {highest_num}.")
            continue

        if guess < answer:
            print("Too low. Try again.")
        elif guess > answer:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You've guessed the number {answer} correctly!")
            is_running = False
    except ValueError:
        print("Invalid input. Please enter a valid integer.")