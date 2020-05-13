from copy import copy, deepcopy
import json


print("\n")
print("##############################")
print("#    List of Dictionaries    #")
print("##############################\n")

# Create three dictionaries holding device information for specific devices
dev30 = {'name':'xrv-0','ip':'10.1.1.30','user':'cisco'}
dev31 = {'name':'xrv-1','ip':'10.1.1.31','user':'cisco'}
dev32 = {'name':'xrv-2','ip':'10.1.1.32','user':'cisco'}

# Create a list to hold information about all of my devices created above
dev_list = [i for i in range(3)]
dev_list[0] = dev30 # sets list item 0 to dictionary dev30
dev_list[1] = dev31 # sets list item 1 to dictionary dev31
dev_list[2] = dev32 # sets list item 2 to dictionary dev32

print(dev_list,'\n')

print(json.dumps(dev_list,indent=4),'\n')

print("\n")
print("####################################")
print("#    Dictionary of Dictionaries    #")
print("####################################\n")

dev30 = {'ip':'10.1.1.30','user':'cisco'}
dev31 = {'ip':'10.1.1.31','user':'cisco'}
dev32 = {'ip':'10.1.1.32','user':'cisco'}
devices = {}
devices['xrv-0'] = dev30 # sets item 'xrv-0' to dev30
devices['xrv-1'] = dev31 # sets item 'xrv-1' to dev31
devices['xrv-2'] = dev32 # sets item 'xrv-2' to dev32

print(devices,'\n')
print(json.dumps(devices,indent=4),'\n')

print("\n")
print("#############################################")
print("#    Dictionary of Lists of Dictionaries    #")
print("#############################################\n")

# Create dictionaries holding device information for these three XRv devices
dev30 = {'name':'xrv-0','ip':'10.1.1.30','user':'cisco'}
dev31 = {'name':'xrv-1','ip':'10.1.1.31','user':'cisco'}
dev32 = {'name':'xrv-2','ip':'10.1.1.32','user':'cisco'}
# Create a list for our XRv devices that we have just defined
xrv_devices = []
xrv_devices.append(dev30)
xrv_devices.append(dev31)
xrv_devices.append(dev32)

nx_devices=[]
ios_devices=[]

all_devices = {'xrv':xrv_devices,'nx-os':nx_devices,'ios':ios_devices}  # all IOS devices go here
print(all_devices,'\n')

print(json.dumps(all_devices,indent=4))
