# Electric Current in Three Phase
v=int(input("Enter voltage: "))
I=int(input("Enter Current: "))
PF=int(input("Enter Power Factor: "))
Kw=(v*I*PF*1.732)//1000
print("Electric current in three phase:", Kw)
