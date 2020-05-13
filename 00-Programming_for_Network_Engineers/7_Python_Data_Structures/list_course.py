print('##################################')
print("#    Creation d'une liste vide   #")
print('##################################')
print('\n')

my_list=list()
my_list_2=[]

print(my_list)
print(my_list_2)

print('\n')
print('##################################')
print("#    Creation d'une liste        #")
print('##################################')
print('\n')

dev_info = ['10.3.21.5', 'username', 'password']

print(dev_info)

print('\n')
print('##################################')
print("#    conversion d'un tuple        #")
print("#        en liste                #")
print('##################################')
print('\n')

device_tuple = ('10.3.21.5', 'username', 'password')
print(device_tuple)
device_list=list(device_tuple)

print(device_list)

print('\n')
print('##################################')
print("#    conversion d'un stri        #")
print("#        en liste                #")
print('##################################')
print('\n')

device_string='10.3.21.5 ,username, password    '
device_list = device_string.strip().split(',')

print(device_string)
print(device_list)

print('\n')
print('##################################')
print("#         add item in            #")
print("#           a liste              #")
print('##################################')
print('\n')

device_types = ['IOS','XR'] # create list
device_types.append('XE') # add 'XE' to list

print(device_types)

print('\n')
print('##################################')
print("#         insert item in         #")
print("#           a liste              #")
print('##################################')
print('\n')

device_types.insert(2,'NX')
print(device_types)

print('\n')
print('##################################')
print("#         removing item in       #")
print("#           a liste              #")
print('##################################')
print('\n')

device_types.remove('NX')
print(device_types)

del device_types[0]
print(device_types)

print('\n')
print('##################################')
print("#         popping item in       #")
print("#           a liste              #")
print('##################################')
print('\n')

item = device_types.pop()

print(type(item))
print(item)
