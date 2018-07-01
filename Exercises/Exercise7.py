#List Comprehension

# Let’s say I give you a list saved in a variable: 
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a 
# and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in a:
    if(i%2 == 0):
        print('{0} is even.'.format(i))
    else:
        print('{0} is odd'.format(i))

b = [i for i in a if i%2 == 0]
print(b)