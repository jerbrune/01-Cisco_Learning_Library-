class networkDevice:
    def __init__(self,name,ip,username = 'cisco',pwd = 'cisco'):
        self.name = name
        self.ip_address = ip
        self.username = username
        self.password = pwd
        self.os_type = 'unknown'

class iosDevice(networkDevice):
    def __init__(self,name,ip,username = 'cisco',pwd = 'cisco'):
        networkDevice.__init__(self,name,ip,username,pwd)
        self.os_type = 'ios'

class ios_xrDevice(networkDevice):
    def __init__(self,name,ip,username,pwd):
        networkDevice.__init__(self,name,ip,username,pwd)
        self.os_type = 'ios-xr'

def read_device_info(devices_file):
    devices_list =[]

    file = open(devices_file, 'r')
    for line in file:
        device_info = line.strip().split(',')
        if device_info[1] == 'ios':
            device = iosDevice(device_info[0],device_info[2],device_info[3],device_info[4])
        elif device_info[1] == 'ios-xr':
            device = ios_xrDevice(device_info[0],device_info[2],device_info[3],device_info[4])
        else:
            continue
        devices_list.append(device)

    file.close()
    return devices_list

def print_device_info(devices_list):
    print('')
    print('{0:11}{1:11}{2:18}{3:11}{4:11}'.format('Name','OS-type','IP address','Username','Password'))
    print('-'*59)

    for device in devices_list:
        print('{0:11}{1:11}{2:18}{3:11}{4:11}'.format(device.name,device.os_type,device.ip_address,device.username,device.password))
    
    print('')

def main():
    device_list = read_device_info('device.txt')
    print_device_info(device_list)

if __name__=='__main__':
    main()

