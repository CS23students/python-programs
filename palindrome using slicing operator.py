name=input("Enter a string: ")
a=str(name)
reverse=a[::-1]
if (a==reverse):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
