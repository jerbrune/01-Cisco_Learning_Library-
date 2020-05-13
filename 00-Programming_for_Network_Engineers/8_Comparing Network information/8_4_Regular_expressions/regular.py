import re
import paramiko

version_pattern = re.compile('Version ([0-9]*\.[0-9]*\.[0-9])')
file=open('showVersion.txt','r')

show_version=file.read()
print(show_version)

version = version_pattern.search(show_version)
version_string = version.group(0)
print(version)
print(version_string)
    

   



