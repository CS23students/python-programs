# largest number in a list using function

def max(l):
    max=l[0]
    for i in l:
        if i>max:
            max=i
    print("largest number in the list is:",max)
list=[45,9,23,45,96]
max(list)

