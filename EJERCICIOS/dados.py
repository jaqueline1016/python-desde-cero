import random

#print("\u25CF \u250C \u2510 \u2502 \u2514 \u2518")
# ● ┌ ┐ │ └ ┘

#┌───────────────┐
#│               │
#│               │
#│               │
#│               │
#└───────────────┘

dice_art = {
    1: (
        "┌───────────────┐",
        "│               │",
        "│       ●       │",
        "│               │",
        "└───────────────┘",
    ),
    2: (
        "┌───────────────┐",
        "│   ●           │",
        "│               │",
        "│           ●   │",
        "└───────────────┘",
    ),
    3: (
        "┌───────────────┐",
        "│   ●           │",
        "│       ●       │",
        "│           ●   │",
        "└───────────────┘",
    ),
    4: (
        "┌───────────────┐",
        "│   ●       ●   │",
        "│               │",
        "│   ●       ●   │",
        "└───────────────┘",
    ),
    5: (
        "┌───────────────┐",
        "│   ●       ●   │",
        "│       ●       │",
        "│   ●       ●   │",
        "└───────────────┘",
    ),
    6: (
        "┌───────────────┐",
        "│   ●       ●   │",
        "│   ●       ●   │",
        "│   ●       ●   │",
        "└───────────────┘",
    ),
}

dice  =  []
total  =0 
num_of_dice =  int(input("How many dice? "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Se imprime para abajo 
#for die in range(num_of_dice):
#    for line in dice_art[dice[die]]:
#         print(line)

# Se imprime para lado a lado
for line in range(5):
    for die in dice:
        print(dice_art[die][line], end=" ")
    print()

for die in dice:
    total += die

print(f"total: {total}")