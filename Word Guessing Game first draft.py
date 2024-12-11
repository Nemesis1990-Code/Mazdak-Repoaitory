import random
print("")
print("Welcome to Word Guessing game!")
print("")
print("We will generate a 4, 5 or 6 letters word based on the difficulty level you choose.")
print("")
print("You can guess the word letter by letter. Every wrong try will decrease 5 points from your initial 500!")
print("")
print("Good luck and have fun!")
print("")
print("Now select your difficulty level!")
print("")


# alphabet = 'abcdefghijklmnopqrstuvwxyz'

while True:

    difficulty = input("Enter 1 for easy 2 for medium or 3 for hard: ")
    print("")

    if difficulty == "1":

        word_length = 4

        print("The word has 4 letters!")
        print("")
        break

    elif difficulty == "2":

        word_length = 5

        print("The word has 5 letters!")
        print("")
        break

    elif difficulty == "3":

        word_length = 6

        print("The word has 6 letters!")
        print("")
        break

    else:
        print("Invalid input!")
        print("")

random_word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(word_length))
# print(random_word)
    
score = 500
attempts = 0
guessed_word = ["_"] * word_length

print("Now it's time to guess a letter and we will tell you if it's included in the random word or not")
print("Guess the word: " + " ".join(guessed_word))
print("")

while score > 0 and "_" in guessed_word:

    guess = input("Enter your guess (a single letter): ").lower()

    if guess in random_word:
        for i in range(word_length):
            if random_word[i] == guess:
                guessed_word[i] = guess
        print("Correct! " + " ".join(guessed_word))
        print("")
    else:
        attempts += 1
        score -= 5
        print(f"Wrong Guess! 5 points lost! Current score: {score}")
        print("")
    
    if "_" not in guessed_word:
        print(f"Congratulations! You solved the puzzele! The word is {random_word}.")
        break
if "_" in guessed_word:
    print(f"Game is over! You have 0 points left! The word was {random_word}.")
print(f"Your final score is: {score}")


   



