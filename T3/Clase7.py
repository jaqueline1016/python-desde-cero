# membership operators: in, not in


word = "apple"

letter =  input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter} in the word")
else:
    print(f"There is no {letter} in the word")

#------------------------

students = {"John", "Emily", "Michael"}

student = input("Enter a student's name: ")

if student not in students:
    print(f"{student} is not in the class.")
else:
    print(f"{student} is in the class.")


# match-case

def day_of_week(day_number):
    match day_number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number"
        
day_number = int(input("Enter a day number (1-7): "))
print(day_of_week(day_number))



# module 
#print(help("modules"))