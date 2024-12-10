import random

#Introduction

print("")
print("welcome to the Number Guessing Game!")
print("")
print("I have selected a number and you will have 10, 7 or 5 attempts both based on the difficulty level to guess my number!")
print("")
print("Good luck and have fun :)")
print("")

#Difficulty levels

print("Choose a difficulty level:")
print("")
print("Enter 1 for easy")
print("")
print("You will have 10 attempts to guess the number between 1 and 50")
print("")
print("Enter 2 for medium")
print("")
print("You will have 7 attepmts to guess the number between 1 and 100")
print("")
print("Enter 3 for Hard")
print("")
print("You will have 5 attempts to guess the number between 1 and 200")
print("")
print("Now choose your difficulty: ")
print("")

while True:

    difficulty = input()
    print("")

    if difficulty in ["1", "2", "3"]:
        break

    else:
        print("Invalid input! Please enter 1, 2, or 3")


if difficulty == "1":
    
    attempts = 10
    goal = random.randint(1, 50)
    max_range = 50

elif difficulty == "2":

    attempts = 7
    goal = random.randint(1, 100)
    max_range = 100

else:

    attempts = 5
    goal = random.randint(1, 200)
    max_range = 200

print(goal)
print(max_range)
print("")

for i in range(attempts):
    while True:
        try:
            guess = int(input("Enter your guess: "))
            print("")

            if 1 <= guess <= max_range:

                break

            else:

                print(f"please enter a number between 1 and {max_range}")
                print("")

        except ValueError:

            print("")
            print("Please enter a valid integer number!")
            print("")

    if guess < goal:

        if i < attempts - 1:

            print("Ouch! Wrong!")
            print("")
            print("tip: It's higher ;)")
            print("")
            print(f"You have {attempts - i - 1} attempts left ")
            print("")

    elif guess > goal:

        if i < attempts - 1:

            print("Ouch! Wrong!")
            print("")
            print("tip: It's lower ;)")
            print("")
            print(f"You have {attempts - i - 1} attempts left ")
            print("")

    else:

        print("congratulations! Your guess is correct! ")
        print("")
        
        break

if guess != goal:
    print(f"sorry, you ran out of attempts! The number was: " , goal)
