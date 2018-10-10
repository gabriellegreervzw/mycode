#!/usr/bin/env python3
loginfail = 0
loginsuccessful = 0

keystone_file = open('/Users/greerga/home/student/mycode/attemptlogin/keystone.common.wsgi', 'r')
keystone_file_lines = keystone_file.readlines()

for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 
        ip_add = keystone_file_lines[i].split(' ', -1)
        print(ip_add[-1])
    elif "-] Authorization failed" in keystone_file_lines[i]:
        loginsuccessful +=1
print('The number of failed log in attempts is ' + str(loginfail))
print('The number of successful login attempts in ' + str(loginsuccessful))
        
