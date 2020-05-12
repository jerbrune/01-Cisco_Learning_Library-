class NetworkDevice:
    def __init__(self,name,os_type,ip_addr,user='cisco',pw='cisco'):
        self.name = name
        self.os_type = os_type
        self.ip_addr = ip_addr
        self.user_name = user
        self.password = pw