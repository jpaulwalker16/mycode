#!/usr/bin/env python3
#GOAL is to use metadata to copy over a file

import paramiko
import os

t= paramiko.Transport("10.10.2.3",22) #port number and IP number

t.connect(username="bender", password="alta3")#how to connect

sftp = paramiko.SFTPClient.from_transport(t) #makesftp connection object

#iteration across files within directory
for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connections
sftp.close() # close the connection
t.close()

