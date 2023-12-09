import math
n=int(input("Enter limit: "))
x=int(input("Enter degree: "))
x=x*(3.14/180)
p=1
f=1
s=x
sine=-1
for i in range (3,n+1,2):
    x=x*sine
    p=pow(x,i)
    f=f*i*(i-1)
    s=s+(p/f)
    print(s)
