class NetworkDevice:
    def __init__(self,name,os_type,ip_addr,user='cisco',pw='cisco'):
        self.name = name
        self.os_type = os_type
        self.ip_addr = ip_addr
        self.user_name = user
        self.password = pw
    
    def print_info_device(self):
        print('{0:11}{1:11}{2:18}{3:18}{4:11}'.format("Name","OS Type","IP address", 'user name','password'))
        print("-"*67)
        print('{0:11}{1:11}{2:18}{3:18}{4:11}'.format(self.name,self.os_type,self.ip_addr,self.user_name,self.password))


def print_device_info(devices_list):
    print('{0:11}{1:11}{2:18}{3:18}{4:11}'.format("Name","OS Type","IP address", 'user name','password'))
    print("-"*67)
    for device in devices_list:
        print('{0:11}{1:11}{2:18}{3:18}{4:11}'.format(device.name,device.os_type,device.ip_addr,device.user_name,device.password))



device1=NetworkDevice('Dev1','IOS_XE','10.1.1.1')
device2=NetworkDevice('Dev2','NX-OS','20.1.1.1','Admin','C1sc0123')
print_device_info([device1,device2])