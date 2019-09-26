#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

cisco1 = {
    "host": "cisco1.twb-tech.com",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

net_connect = Netmiko(**cisco1)

# Create a List of Cisco commands that can be used later in a 'FOR' loop
commands = [
"terminal length 0",
"show ip int brief",
"show version",
"show vlan brief",
"teminal length 24",
]

# Create a function with two required inputs called  that will used repeatably 
def showCommands(profile, cmds):
    for items in cmds:
        print(profile.find_prompt())
        output = profile.send_command(items)
        print(output + "\n\n")
    profile.disconnect()



# By calling the function, with the required inputs "profile" and "cmds"
# This function will start the "FOR" loop and execute the "show commands"
#     in the LIST called, "commands".
showCommands(net_connect, commands)
