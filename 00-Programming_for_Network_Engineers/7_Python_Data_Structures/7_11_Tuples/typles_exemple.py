my_tuple = tuple()
print(type(my_tuple))
my_tuple = 'test','test2',"['a','b']"

print(my_tuple[0])

string='test'
print(type(string))
s=string.split()
print(s)
string2=str()
print(type(string2))
for i in string:
    print(i)
    string2+=i
print(string2)
devices_list = ['xr','nx','nx','xe','xr','nx','xr','ios','nx','xe','xr','xr','nx']
dev_os_types=set(devices_list)

print(dev_os_types)