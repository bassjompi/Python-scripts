#!/usr/bin/python

import os
import subprocess


for root, dirs, files  in os.walk('/Users'):
    for file in files:

        if file.endswith('.pgp') or file.endswith('.PGP') or file.endswith('.gpg'):
            deleter =(os.path.join(root,file))

            print ('do you want to delete the file {0}? '.format(deleter))
            choice = raw_input('y/n\n')
            if choice == 'y':
                os.remove(deleter)