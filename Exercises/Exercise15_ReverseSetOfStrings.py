# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.


inputStr = "My name is Paolo"

def reverseString(str = ""):
    listStr = str.split(" ")
    listStr.reverse()
    return " ".join(listStr)

print(reverseString(inputStr))