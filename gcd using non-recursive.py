# gcd using non recursive
def gcd(a,b):
    if a<b:
        min=a
    else:
        min=b
    for i in range(1,min+1):
        if(a%i==0 and b%i==0):
            hcf=i
    return hcf 
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Gcd of",a,"and",b,"is",gcd(a,b))
 
