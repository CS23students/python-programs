# square root using newton's method for loop
def sq_root(n,l):
    a=n*0.5
    for i in range(l):
        root=0.5*(a+(n/a))
        a=root
    return a
n=int(input('Entr the number: '))
l=int(input('Enter the base: '))
print('square root of',n,'is',sq_root(n,l))
