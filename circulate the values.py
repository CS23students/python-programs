
# Circulate the values of n
n=[1,2,3,4,5]
a=int(input("Enter circulations: "))
for i in range (0,a+1):
    b=n[i:]+n[:i]
    print(b)
