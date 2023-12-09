# binary search non recursive
def binarySearch(l,k):
    low=0
    high=len(l)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if l[mid]==k:
            return mid
        elif l[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return -1
l=[12,32,4,6]
k=int(input('Enter the search element: '))
result=binarySearch(l,k)
if result<0:
    print('Element not found')
else:
    print('Element found at position',result+1)
