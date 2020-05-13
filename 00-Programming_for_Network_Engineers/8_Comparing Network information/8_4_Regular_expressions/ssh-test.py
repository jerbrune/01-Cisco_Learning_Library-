import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname='ios-xe-mgmt.cisco.com',username='developer', password='C1sco12345',port='8181')
stdin, stdout, stderr = ssh_client.exec_command('show version')
ip_route_table = stdout.readlines()
for i in ip_route_table:
    print(i)

ssh_client.close()


