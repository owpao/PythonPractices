import random

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

first = input("Enter first letter: ")
second = input("Enter second letter: ")

firstIndex = alphabet.index(first.upper())
secondIndex = alphabet.index(second.upper())+1
letterList = {}

for x in range(firstIndex, secondIndex):
    value = []
    for i in range(0, random.randint(1,10)):
        value.append(alphabet[x])
    letterList[alphabet[x]] = value

for letter in letterList:
    print("'"+letter+ "': "+ str(letterList[letter]))
