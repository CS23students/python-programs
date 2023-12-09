# list operations
lst=[1,2,4,'abc','xyz']
lst2=[2,4,10,1]
lst.append('efg')
print('1.append: ',lst)
lst.extend([5,6])
print('2.extend: ',lst)
lst.insert(2,3)
print('3.insert: ',lst)
lst.pop(6)
print('4.pop: ',lst)
print('length: ',len(lst))
lst2.sort()
print('sort: ',lst2)
print('concate: ',lst+lst2)
lst2=lst.copy()
print('copy: ',lst2)

