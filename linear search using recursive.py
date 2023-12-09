# linear search using recursive
def linearSearch(l,k,i):
    if i==0:
        return -1
    elif l[i-1]==k:
        return i-1
    return linearSearch(l,k,i-1
                        )
l=[1,10,12,32,9]
k=int(input('Enter the search element: '))
i=len(l)
result=linearSearch(l,k,i)
if result<0:
    print('Element not found')
else:
    print('Element found at position',result+1)
