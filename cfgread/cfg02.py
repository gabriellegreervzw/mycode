#!/usr/bin/env python3
## create file object in "r"ead mode
name_of_file = input('what is the name of your file')
configfile = open(name_of_file, 'r')

configlines = configfile.readlines()
print(configlines)
counter = 0
for i in range(len(configlines)):
    counter += 1
print(counter)

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no '\n'
print(configlist)

## Always close your file
configfile.close()

