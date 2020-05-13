file=open("showVersion.txt",'r')

print('#######################')
print('#      READLINES      #')
print('#######################')
print('\n')
my_input = file.readlines()

print(type(my_input))
print('\n\n')

for i in my_input:
    print(i)

file.close()

print('\n')
print('#######################')
print('#      READLINE       #')
print('#######################')
print('\n')

file=open("showVersion.txt",'r')
for line in file:
    my_input = file.readline()
    print(my_input) 

file.close()


print('\n')
print('#######################')
print('#         READ        #')
print('#######################')
print('\n')

file=open("showVersion.txt",'r')
my_input=file.read(100)
print(type(my_input))
print("\n",my_input)
file.close()


print('#######################')
print('#      READLINE       #')
print('#      + strip()      #')
print('#######################')
print('\n')

file = open("showVersion.txt",'r')

for line in file:
    my_input = file.readline()
    print(my_input)

file.close()

print('#######################')
print('#      Writing in     #')
print('#      a new file     #')
print('#######################')
print('\n')

file = open('new_file.txt','a')
my_string = "première entrée\ndeuxième entée"
file.writelines(my_string)
file.close()