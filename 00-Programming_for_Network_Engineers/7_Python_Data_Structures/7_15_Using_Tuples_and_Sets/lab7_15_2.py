from collections import namedtuple
from pprint import pprint

dev_info =namedtuple('dev_info',['name','os','ip','user','password'])
devices_info={}

file=open('device.txt','r')

for line in file:
    device_info = dev_info(*(line.strip().split(',')))
    devices_info[device_info.name]=device_info
    
pprint(devices_info) 
file.close()
