rows = int(input("Enter Sandglass Star Pattern Rows = "))

print("Sandglass Star Pattern")

for i in range(0, rows):
    for j in range(0, i):
        print(end = ' ')
    for k in range(i, rows):
        print('*', end = ' ')                
    print()

for i in range(rows - 1, -1, -1):
    for j in range(0, i):
        print(end = ' ')
    for k in range(i, rows):
        print('*', end = ' ')      
    print()
