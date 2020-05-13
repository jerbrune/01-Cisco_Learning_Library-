device_string = '  1.1.1.1, username  , password   '
device_list = device_string.split(',')
print (device_list)
info_list=list()
for item in device_list:
    item = item.strip()
    info_list.append(item)

print (info_list)