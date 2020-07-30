#!/usr/bin/python python
#test.py
#anubhav

import time as t



print ("hello world!")
print ("current time as t: " + t.ctime())
name = input("Please enter your name \n")
if (len(name) > 0):
	print ("hello " + name)
else:
	print ("not a valid name")

