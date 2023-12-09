# linear search non recursive
def linearSearch(l,k):
    for i in range(len(l)):
        if l[i]==k:
            print('Element found at position',i+1)
            break

    else:
            print('Element not found')
l=[12,32,43,1]
k=int(input('Enter the search element: '))
linearSearch(l,k)
