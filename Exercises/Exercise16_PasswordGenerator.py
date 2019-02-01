# Write a password generator in Python. Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

import random

CHARACTERS_SMALL = "abcdefghijklmnopqrstuvwxyz"
CHARACTERS_CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()_+"
simpleWords = ["password", "12344321", "admin"]


def main():

    print("---- Password Generator ----")
    print("[1] Weak Password")
    print("[2] Strong Password")
    print("[0] Exit")

    key = input("\nEnter option: ")
    if(key == "1"):
        weakPassword()
    elif(key == "2"):
        strongPassword()
    else:
        pass


def weakPassword():

    index = 1
    for o in simpleWords:
        print(index, " ", o)
        index += 1

    key = int(input("\n\nChoose a password from the list: "))
    if(key > 0 & key <= 3):
        print("Your password is: ", simpleWords[key-1])
    else:
        print("You entered a wrong option!")


def strongPassword():
    password = ""
    for i in range(0, random.randint(10, 15)):
        charSelector = random.randint(1, 4)
        if (charSelector == 1):
            password += CHARACTERS_CAPS[random.randint(
                0, len(CHARACTERS_CAPS)-1)]
        elif (charSelector == 2):
            password += CHARACTERS_SMALL[random.randint(
                0, len(CHARACTERS_SMALL)-1)]
        elif (charSelector == 3):
            password += NUMBERS[random.randint(0, len(NUMBERS)-1)]
        elif (charSelector == 4):
            password += SYMBOLS[random.randint(0, len(SYMBOLS)-1)]

    print("Your password is: ", password)


if __name__ == "__main__":
    main()
