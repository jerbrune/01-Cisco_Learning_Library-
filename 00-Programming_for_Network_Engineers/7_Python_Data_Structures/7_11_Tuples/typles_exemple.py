from collections import namedtuple

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
Info = namedtuple('Info',['name','version'])
dev_info = Info(name='iosxrv1', version='A.01.01')
version = dev_info.version
print(namedtuple.__doc__)

print(version)

print(dev_info.__doc__)
