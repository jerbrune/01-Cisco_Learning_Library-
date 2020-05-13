from pprint import  pprint
import json

file = open('devices.txt','r')

device_string = file.readline().strip()
device_list = device_string.split(',')


pprint(device_list)

for item in device_list:
    print(item)


device_desc={}
device_desc['name']=device_list[0]
device_desc['OS']=device_list[1]
device_desc['IP'] = device_list[2]
device_desc['user'] = device_list[3]
device_desc['pwd']=device_list[4]

pprint(device_desc)

file.close()

file = open('devices.txt','r')
devices_info={}
for line in file:
    device_list=line.strip().split(',')
    device_info = { }  # Create the inner dictionary of device info
    #device_info['name'] = device_list[0]
    device_info['os-type'] = device_list[1]
    device_info['ip'] = device_list[2]
    device_info['username'] = device_list[3]
    device_info['password'] = device_list[4]
    devices_info[device_list[0]] = device_info


pprint(devices_info)
print(json.dumps(devices_info,indent=4))

file.close()

file = open('devices.txt','r')
devices={}
devices['IOS']=[]
devices['NX-OS']=[]
devices['IOS-XR']=[]

device_list=list()
for line in file:
    device = line.strip().split(',')
    device_info=dict()
    device_info['name'] = device[0]
    device_info['os-type'] = device[1]
    device_info['ip'] = device[2]
    device_info['username'] = device[3]
    device_info['password'] = device[4]
    device_list.append(device_info)

for item in device_list:
    if item['os-type']=="ios":
        devices['IOS'].append(item)
    elif item['os-type']=="nx-os":
        devices['NX-OS'].append(item)
    else:
        devices['IOS-XR'].append(item)

print(json.dumps(devices,indent=4))
