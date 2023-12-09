n=int(input("Enter rows: "))
i=0
while i<n:
    j=0
    while j<i:
        print("",end=" ")
        j=j+1
    k=0
    while(k<n-i):
        print("*",end='')
        k+=1
    print(' ')
    i+=1
