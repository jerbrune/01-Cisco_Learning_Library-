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
file=""
for i in ip_route_table:
    file+= i
version = version_pattern.search(file)
version_string = version.group(0)

print(version_string)

ssh_client.close()


