# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

import random

def returnFirstAndLastElements(myList=[]):
    newList = []
    newList.append(myList[0])
    newList.append(myList.pop())

    return newList

def createRandomList():
    newList = []

    for i in range (0,random.randint(10,15)):
        newList.append(random.randint(1,25))
    
    return newList


myList = createRandomList()
print("My generated list: ", myList)
print(returnFirstAndLastElements(myList))