#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - testing if strings test true"""

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

#splitting input
a=ipchk.split('.')
print(a)
if len(a)==4:
    print(" ")

else:
    print("re-enter a valid ip address")
    
# a provided string will test true
if ipchk:
   print("Looks like the IP address was set: " + ipchk) # indented under if
else:
    print('user failed to input ip value')

