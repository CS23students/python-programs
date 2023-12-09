a=(input("enter the string:"))
b=(input("enter the character:"))
count=0
for i in a:
    if i==b:
        count+=1
print("the no of times ",b,"appear is",count)
if count==0:
    print("the character is not in the string")
