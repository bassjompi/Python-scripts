#!/usr/bin/python

import os

hostname = 'www.google.com'
response = os.system('ping -c 1 ' + hostname)

if response == 0:
    print ('\ntalend is up')

elif response == 1:
    print ('talend is down')