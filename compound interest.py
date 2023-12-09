# Compound Interest
p=int(input("Enter Amount: "))
r=float(input("Enter Rate %: "))
t=float(input("Enter Time period: "))

c=p*(((1+r/100)**t)-1)
print("The compound interest: ",c)
