# Operations on Tuple

t1=(10,11,31,41,30)
t2=('abc','efg','xyz')
print('length: ',len(t1))
print('Minimum: ',min(t1))
print('Maximum: ',max(t1))
print('Count: ',t1.count(11))
print('Multiply: ',t1*2)
print('Concate: ',t1+t2)
print('Memership: ',31 in t1)
print('Slice: ',t2[0:1])

print('-'*50)
tuple_1=('A','B','C','D')
tuple_2=(1,2,3)
list1=[1,2,3,4,5]
print('list to tuple: ',tuple(list1))
print('String to tuple: ',tuple('Apple'))
print('Concate: ',tuple_1+tuple_2)
print('Repetition: ',tuple_2*3)
print('Slicing: ',tuple_1[0:2])
print('Membership: ','c' in tuple_1)
