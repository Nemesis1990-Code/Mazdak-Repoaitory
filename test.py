import random
goal = random.randint(1, 100)
for i in range(5):
    guess = int(input("Enter Your Guess: "))
    print("")
    if guess < goal:
        print("Higher!")
        print('')
    elif guess > goal:
        print("lower")
        print("")
    else:
        print("Congratulations! That's the correct number ")
        print("")
        break
if guess !=goal :
    print(" Sorry you are ran out of attempts. the correct number was: " , goal)

