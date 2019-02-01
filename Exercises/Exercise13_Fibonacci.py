#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is 
# the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

fibList = []
def fibonacci(n = int):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

numOfNumbers = int(input("How many numbers do you want to generate in fibonacci? :"))
for i in range(1,numOfNumbers+1):
    fibList.append(fibonacci(i))

print(fibList)