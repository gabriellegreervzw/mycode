#!/usr/bin/env python3

# function to push commands
def commandpush(devicecmd): # devicecmd==list 
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            print('\n', end='')
            # we'll learn to write code that sends cmds to device here
y = 0
file_dict = {}
test_file = open('test_commands.txt', 'r')
test_file_lines = test_file.readlines()
#print(str(len(test_file_lines)))
for x in range(0,len(test_file_lines),3):
    y = x + 1
#    print('x is: ' + str(x))
    #print('y is: ' + str(y))
    if (x <= len(test_file_lines) and y < len(test_file_lines)-1):
        file_dict.update({test_file_lines[x].strip(): [test_file_lines[y].strip(), test_file_lines[y+1].strip()]})
    else:
        break
    x = y + 2
    #print('x is: ' +str(x))

#print(file_dict) 
    

### Start our script
#work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} # data that replaces data stored in file

work2do = file_dict

print("Welcome to the network device command pusher") # welcome message

## get data set
print("\nData set found\n") # replace with function call that reads in data from file

## run 
commandpush(work2do) # call function to push commands to devices

def devicereboot(iplist):
    for i in iplist:
        print("Connecting to...." + i)
        print ("REBOOTING NOW!")

test_ip_loop = ['10.123.123.10', '10.142.122.75']
devicereboot(test_ip_loop)
