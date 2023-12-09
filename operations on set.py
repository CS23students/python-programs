print('Add element to the set:')
set1=set()
n=int(input('Enter the no. the set Elements:'))
for i in range(1,n+1):
    set1.add(i)
print('set1: ',set1)
print('\nUpdate Element to the set')
a={'apple','orange','grape'}
b={'red','pink','yellow'}
print('Before update set: ',a )
a.update(b)
print('After update set: ',a)
print('\nRemove the elements from the set')
s={2,4,7,1,5}
print('Initial set: ',s)
s.remove(2)
print('Set after remove(): ',s)
s.discard(7)
print('Set after discard: ',s)
s1={2,5,6,7,9}
s2={1,2,4,6}
print('\nSet1: ',s1)
print('Set2: ',s2)
print('\nUnion of two sets:')
print('Using | method: ',s1|s2)
print('using union() Method: ',s1.union(s2))
print('\nIntersection of two sets:')
print('Using & method: ',s1&s2)
print('using intersection() Method: ',s1.intersection(s2))
print('\nDifference of two sets:')
print('Using - method: ',s1-s2)
print('using difference() Method: ',s1.difference(s2))
print('\nSymmetric difference of two sets:')
print('Using ^ method: ',s1^s2)
print('using symmetric_difference() Method: ',s1.symmetric_difference(s2))
print('\nSet Comparisons')
print('s1>s2: ',s1>s2)
print('s1<s2: ',s1<s2)
print('s1>=s2: ',s2>=s2)
print('s1<=s2: ',s1<=s2)
print('s1==s2: ',s1==s2)
print('s1!=s2: ',s1!=s2)


