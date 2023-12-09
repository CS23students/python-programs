name=input("Enter a string: ")
seq=str(name)
if (seq=="".join(reversed(seq))):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
    
