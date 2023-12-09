# reverse of a string

# using for loop
print('Using for loop')
a=input('Enter the string: ')
s=''
for i in a:
    s=i+s
print('The reverse of a string is',s)

# using slicing
print('\nUsing Slicing')
a=input('Enter the string: ')
b=a[::-1]
print('The reverse of a string',b)

# using reverse()
print('\nUsing reverse()')
a=input('Enter the string: ')
b=''.join(reversed(a))
print('The reverse of a string:',b)
