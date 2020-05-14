from pprint import pprint

file = open('device.txt','r')

devices_list=[]
for line in file:
    device_info =tuple(line.strip().split(','))
    devices_list.append(device_info)


pprint(devices_list)

file.close()
