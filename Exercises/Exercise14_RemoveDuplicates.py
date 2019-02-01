# Write a program (function!) that takes a list
# and returns a new list that contains all the
# elements of the first list minus all the duplicates.


def removeDuplicatesUsingLoop(numList=[]):
    newList = []
    for i in numList:
        if(newList.count(i) < 1):
            newList.append(i)

    return newList


def removeDuplicatesUsingSets(numList=[]):
    newSet = set()
    for i in numList:
        newSet.add(i)

    return newSet


sampleList = [0, 0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6, 7, 8, 8, 8, 9, 10]
print("Sample List: ",sampleList)
print(removeDuplicatesUsingLoop(sampleList))
print(removeDuplicatesUsingSets(sampleList))
