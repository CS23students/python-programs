# count of a string

# using for loop
print('Using for loop')
a=input('Enter the string: ')
b=input('Enter the character: ')
count=0
for i in a:
    if i==b:
        count+=1
        print('The no. of times',b,'is',count)
if count==0:
        print('The character is not found in the string')

# using count function
print("\nUsing count function")
a=input('Enter the string: ')
b=input('enter the character: ')
c=a.count(b)
print('The number of times',b,'is',c)


# using counter
print('\nUsing counter')
from collections import Counter
a=input('Enter the string: ')
b=Counter(a)
print(b)
