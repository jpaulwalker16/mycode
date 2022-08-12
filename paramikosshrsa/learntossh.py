#!/usr/bin/env python3

#issuing commands across a SSH channel

import os
import paramiko

#shortcut issuing commands to remote
def commandissue(command_to_issue, sshsession):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read() # <-- so what's being returned is the stdout from bender
                             # but to see what's in the ssh_stdout object, we used .read() to pull out
                             # the contents
                             # those contents are what are being returned from the function to down below 

def main():
    sshsession = paramiko.SSHClient()

    ############# IF YOU WANT TO CONNECT USING UN/PW ################
    #sshsession.connect(server, username=username, password=password)
    ############## IF USING KEYS ####################################

    ## mykey is our private key
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    ## if we never went to this SSH host, add the fingerprint to the known host file
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ## creds to connect
    sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

    ## a simple list of commands to issue across our connection
    our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]

    ## cycle through our commands and issue them on the far end
    for x in our_commands:
                print(commandissue(x, sshsession).decode('utf-8'))
#<--- so the output from the commandissue() function gets printed here
             # I added the type() function so we can see what exactly that output is
             # what's getting printed out are "bytes", not strings
             # using .decode() on the bytes object returns them as actual human-readable strings
main()
