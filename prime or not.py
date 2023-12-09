n=int(input("Enter the number: "))
r=0
for i in range(2,n):
    if(n%i==0):
        r=1
        break
if(r==0):
    print("The number is prime")
else:
    print("The number is not prime")
