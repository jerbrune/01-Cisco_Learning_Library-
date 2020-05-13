dev1 = {"ip":"10.3.21.5", "version":"A.01.01",  "username":"user1","password":"pw1"}

print(dev1['ip'])

dev1['OS']='NXOS'

print(dev1)

dev1['version']='a.02'

print(dev1)

del dev1['OS']

print(dev1)

if 'ip' in dev1:
    print(dev1['ip'])