from pprint import pprint

file = open('device.txt','r')

devices_list=[]
for line in file:
    device = line.strip().split(',')
    devices_list.append(device)


device_info=tuple(devices_list[0])
pprint(device_info)

file.close()
