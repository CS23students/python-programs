# Inverted pyramid numbers
rows = int(input("Enter number of rows: "))

for i in range(rows, 0,-1):
    for j in range(1, i):
        print(j, end=" ")
    
    print()
