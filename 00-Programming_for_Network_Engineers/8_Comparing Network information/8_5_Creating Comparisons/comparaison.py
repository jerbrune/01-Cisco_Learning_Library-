file = open("devices_list.txt",'r')

print(type(file))

#cont = file.read()
#print(type(cont))
#print(cont)
devices_info=[]
for line in file:
    devices_info.append(line.strip().split(','))

print(type(devices_info))
print(devices_info)

file.close()