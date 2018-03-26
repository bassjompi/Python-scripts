#!/usr/bin/python

import getpass
import pymssql
import sys
from pip.commands.list import tabulate
from Feeds import *

print ('Rollback tool from stage 1 and stage 2 - Accolade')
print ('Juan Pablo Yanez Camacho - Aug. 2017 - v1.0')

phl_server = "PHL-DAQ"

username = raw_input('Please enter your username: ')
user = 'ACCPROD1\%s' % username
password = getpass.getpass()

while True :
	try :
		print ("Connecting to PHL-DAQ....")
		phl_conn = pymssql.connect(phl_server, user, password, "DAQ_STG")
		print ('Connection successfull!')
		break
	except :
		print ('Could not connect to the DB server, please verify your user/password and retry: ')
		username = raw_input('Username: ')
		user = 'ACCPROD1\%s' % username
		password = getpass.getpass()

phl_conn.autocommit(False)

phl = phl_conn.cursor()


filename = raw_input('What is the filename you would like to rollback? (type "exit" for finishing) \n ')

if filename == 'exit':
    phl = phl_conn.close()
    sys.exit(0)

else:
    for filemask in mainlist:                                   ###looks for the filemask

        if filename.startswith(filemask):                       ####filemask found, now iterates in each tablespace

            for element in mainlist[filemask]:

                                                                ####  check if the file is loaded in the table ###
                phl.execute(("""            
                SELECT COUNT(*) FROM %s
                WHERE filename = '%s'
                """) % (element, filename))
                for row in phl:
                    file_validation = row[0]

                    if file_validation == 0:
                        print ('This file is not loaded into {0} table'.format(element))         ### the file is not loaded


                    else:                                        ### the file is in the table

                        while True:

                                option=raw_input('\nAll the records referencing the file {0} are going to be deleted from the table {1}, are you sure you want to continue? (y/n) \n'.format(filename,element))

                                if option == 'y':
                                        phl.execute("""delete from %s where filename ='%s' """ % (element,filename))
                                        phl_conn.commit()
                                        print ('\nThe file {0} has been successfully removed from  {1} table \n'.format(filename,element))
                                        break

                                elif option == 'n':
                                        sys.exit(0)

                                else:
                                        print('Please choose a valid option (y/n)')





phl = phl_conn.close()
sys.exit(0)









