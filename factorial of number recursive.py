# Factorial of a Number Recursive
def fact(n):
    if(n==1):
        return 1
    else:
        return n * fact(n-1)
a=int(input("Enter any number: "))
x=fact(a)
print("The factorial of",a,"is",x)
