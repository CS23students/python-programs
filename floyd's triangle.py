# floyd's triangle
rows=int(input("enter no. of rows: "))
n=1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n+=1
    print()
