from collections import namedtuple
from pprint import pprint
import json

dev_info =namedtuple('dev_info',['name','os','ip','user','password'])
devices_info=set()

file=open('device.txt','r')

for line in file:
    device_info = dev_info(*(line.strip().split(',')))
    devices_info.add(device_info.os)
    
pprint(devices_info) 
#print(json.dumps(devices_info,indent=6))
file.close()
