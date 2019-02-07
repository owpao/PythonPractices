import random

gameStillGoing = bool(True)
numberOfGuesses = int(0)

def generateNumber():
    return random.randint(1000, 9999)


def main():
    secretNumber = str(generateNumber())
    while(gameStillGoing):
        number = input("Guess the secret four digit number: ")

        checkNumberIfMatch(number, secretNumber)


def checkNumberIfMatch(number, secretNumber):
    global numberOfGuesses
    numberOfGuesses+=1
    if(not str(number).isdigit()):
        print("Answer should be a number!")
        return
    elif(len(number) != 4):
        print("Answer should contain four digits!")
        return
    else:
        countCowsAndBulls(number, secretNumber)


def countCowsAndBulls(number, secretNumber):
    cows = int(0)
    bulls = int(0)
    global gameStillGoing

    if(number == secretNumber):
        print("You guessed the correct number!")
        print("Number of guesses: {0}".format(numberOfGuesses))
        gameStillGoing = False
        return
    else:
        for n in range(0, 4):
            if(number[n] == secretNumber[n]):
                cows+=1
            elif(number[n] in secretNumber):
                bulls+=1
        print("Cows: {0}, Bulls:{1}".format(cows,bulls))


if __name__ == "__main__":
    main()
