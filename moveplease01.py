#!/usr/bin/env python3

#local utilities to import
import shutil

#os to us os dep. functionality
import os

#start pt
os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'ceph_storage/')

xname = input( ' what is the new name for kerrigan.obj?')

#rename kerrigan.obj file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' +xname)
