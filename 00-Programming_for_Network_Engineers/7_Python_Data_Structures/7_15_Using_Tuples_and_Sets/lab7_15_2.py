from collections import namedtuple

dev_info =namedtuple('dev_info',['name','os','ip','user','password'])
devices_info={}

file=open('device.txt','r')

for line in file:
    device_info = dev_info(*(line.strip().split(',')))
    #print(line.strip().split(','))
print(device_info) 
file.close()
