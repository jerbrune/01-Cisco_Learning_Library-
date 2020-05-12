import re
import paramiko

version_pattern = re.compile('Version ([0-9]*\.[0-9]*\.[0-9])')
#file=open('show_version.txt','r')

#show_version=file.read()
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname='ios-xe-mgmt.cisco.com',username='developer', password='C1sco12345',port='8181')
stdin, stdout, stderr = ssh_client.exec_command('show version')
ip_route_table = stdout.readlines()
print(ip_route_table)
for i in ip_route_table:
    version = version_pattern.search(i)
    version_string = version.group(2)
    if version != False:
        print(version)
    

   

ssh_client.close()


