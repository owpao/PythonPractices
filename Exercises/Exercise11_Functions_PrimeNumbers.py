
def getInputFromUser():
    return int(input("Enter a number to check if it is prime or not: "))

number = getInputFromUser()
ctr = int(0)

for i in range(number-1,1,-1):
    if(number%i==0):
        ctr+=1

if (ctr>1):
    print(str(number)+" is not a prime number!")
else:
    print(str(number)+" is a prime number!")