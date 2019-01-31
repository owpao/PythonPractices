# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.

import random

randomNumber = random.randint(1, 9)
gameIsStillGoing = True
while gameIsStillGoing:
    answer = int(input("Guess the random number between 1 - 9: "))

    if answer != randomNumber:
        if answer > randomNumber:
            print("Your number is greater than the mystery number!")
        elif answer < randomNumber:
            print("Your number is less than the mystery number!")
    elif answer == "exit":
        gameIsStillGoing = False
    else:
        print("You got the right answer!")
        gameIsStillGoing = False
