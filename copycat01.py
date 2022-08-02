#!/usr/bin/env python3

#import tools needed quickly
import shutil

#import the os module for using os dependent functionality
import os

#starting point for the code
os.chdir("/home/student/mycode/")

#copy the content of the .txt file to .txt.copy file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy recursively the content of 5g to 5g backup directory
shutil.copytree("5g_research/", "5g_research_backup/")

