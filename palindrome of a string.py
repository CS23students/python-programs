# palindrome of a string

# using for loop
print('Using for loop')
a=input('Enter the string: ')
s=''
for i in a:
    s=i+s
if s==a:
    print(s,'is a palindrome')
else:
    print(s,'is not a palindrome')

# using slicing
print('\nUsing slicing')
a=input('Enter the string: ')
b=a[::-1]
if b==a:
    print(b,'is a palindrome')
else:
    print(b,'is not a palindrome')
