name=input("Enter a string: ")
a=""
for i in name:
    a=i+a
if name==a:
    print(f"{name} is palindrome")
else:
    print(f"{name} is not a palindrome")
