import random

#print(help(random))

low = 1
high = 100
option = ("rock","paper","scissors")


#number = random.randint(low,high)
#number  =  random.random()
#options = random.choice(option)
#print(options)
running =  True

while running:

    player =  None
    computer = random.choice(option)

    while player not in option:
        player =  input("Enter a choice (rock, paper, scissors):    ").lower()

    print(f"Player choice: {player}")
    print(f"Computer choice: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")