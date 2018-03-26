#!/usr/bin/python
import sys
import os

print('Talend workspace cleanup - Accolade\nJuan Pablo Yanez - August 2017 - v0.1\n')


while True:
    option = raw_input('This script will delete the workspaces directories and then will REBOOT the machine\nDo you want to continue? (y/n)\n')
    if option == 'n':
        sys.exit()

    elif option == 'y':
        print('\nRemoving workspace directories\n')
        os.system ('rm -rf /app/talend611/cmdline/studio/commandline-workspace')
        os.system('rm -rf /app/talend611/cmdline/studio/workspace')
        os.system('chown -R talenduser:  /app/talend611/cmdline/studio/')

        print('\nThe machine is going to reboot\n')
        os.system('reboot')

    else:
        print('\nPlease specify a valid option y (yes)  or n (no)\n')


