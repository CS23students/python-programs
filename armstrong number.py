# Armstrong Number
num=int(input("Enter any number: "))
sum=0
temp=num
while (num!=0):
    digit=num%10
    sum+=digit**3
    num=num//10
if temp==sum:
        print(temp,"is Armstrong no.")
else:
        print(temp,"is not Armstrong no.")
