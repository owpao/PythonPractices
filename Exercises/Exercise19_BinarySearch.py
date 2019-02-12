from math import ceil

orderedList = [1, 2, 3, 4, 5, 7, 8, 9, 19, 20, 24, 26, 28, 36, 46, 66, 78]
l = [2, 4, 6, 8, 10]


def main():
    if(binarySearch(orderedList, 8)):
        print("Number found!")
    else:
        print("Not found")


def search(list=[], numberToFind=int()):
    if(list.count(numberToFind) > 0):
        return True
    else:
        return False


def binarySearch(list=[], numberToFind=int()):
    startIndex = 0
    endIndex = len(list)-1
    if(list[startIndex]==numberToFind or list[endIndex]==numberToFind):
        return True
    
    while True:
        middleIndex = startIndex+((endIndex-startIndex)//2)
        print("Start Value {0}, Root Value {1}, End Value {2}".format(
            list[startIndex], list[middleIndex], list[endIndex]))
        if middleIndex < startIndex or middleIndex > endIndex or middleIndex < 0:
            return False

        root = list[middleIndex]
        if root == numberToFind:
            return True
        elif root < numberToFind:
            startIndex = middleIndex
        else:
            endIndex = middleIndex


if __name__ == "__main__":
    print(binarySearch(l, 14))
