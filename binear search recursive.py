# binary search recursive
def binarySearch(l,k,low,high):
    mid=0
    while low<=high:
        mid=(low+high)//2
        if l[mid]==k:
            return mid
        elif l[mid]<k:
            return binarySearch(l,k,mid+1,high)
        else:
            return binarySearch(l,k,low,mid-1)
    return -1
l=[1,20,30,50,90]
k=int(input('Enter the search element: '))
low=0
high=len(l)
result=binarySearch(l,k,low,high)
if result<0:
    print('Element not found')
else:
    print('Element found at position',result+1)
