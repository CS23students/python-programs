def fibo(n):
    f1=0
    f2=1
    i=1
    print(f1)
    print(f2)
    while (i<=n):
       f3=f2+f1
       f1=f2
       f2=f3
       print(f3)
       i=i+1
n=int(input("Enter the terms: "))
fibo(n)
