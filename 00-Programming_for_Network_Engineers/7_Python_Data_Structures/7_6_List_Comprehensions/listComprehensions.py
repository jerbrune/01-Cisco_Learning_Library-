device_string = '  1.1.1.1, username  , password   '
device_list = device_string.split(',')
print (device_list)
info_list=list()
for item in device_list:
    item = item.strip()
    info_list.append(item)

print (info_list)
print('')
print('############################')
print('#     List comprehensions  #')
print('############################\n')
info_list_2=[device.strip() for device in device_string.split(',') ]
print (info_list_2)
info_list_2.sort()
print(info_list_2)

