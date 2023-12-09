# square root using newton's method while loop
def sq_root(n,l):
    x=n
    count=0
    while (True):
        count+=1
        root=0.5*(x+(n/x))
        if abs(root-x)<l:
            break
        x=root
    return root
n=int(input('Enter n: '))
l=0.00001
print('square root of',n,'is',sq_root(n,l))
