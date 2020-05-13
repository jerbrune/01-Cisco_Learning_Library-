from copy import copy, deepcopy

print('####################')
print('#    Assignment    #')
print('####################','\n')

device_info=('dev1','10.1.1.1','admin','admin')
d1 = list(device_info)

d2=d1

print(d2,d1)
del d1[0]

print(d1,d2)

print('####################')
print('#   Shallow Copy   #')
print('####################','\n')

d3=copy(d1)
print(d3)
del d1[0]

print(d1,d2)
print(d3)

l1=[[1,2,3],{'a':'1','b':'2'}]
print(l1)

l2=copy(l1)

print(l2)
print(l2[1]['a'])

l2[1]['c']='3'

print(l2)
print(l1)
del l1[1]

print(l1,l2)

print('####################')
print('#     Deep Copy    #')
print('####################','\n')

l4 = deepcopy(l2)
print (l4)
l4[1]['d'] = '4'
print(l4)
print(l2)