#!/usr/bin/python

import getpass
import pymssql
import sys
import time
from Feeds import *

print ('Monitoring tool from stage 1 and stage 2 - Accolade')
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


while True:
	try:
		found = 0
		filename = raw_input('What is the filename you would like to check?  (type "exit" for finishing):\n')

		if filename == 'exit':
			phl_conn.close()
			sys.exit(0)

		else:

			for filemask in mainlist:                                   ###looks for the filemask

				if filename.startswith(filemask):  ####filemask found, now iterates in each tablespace



					for db in mainlist[filemask]:           ####  check if the file is loaded in the table ###
						phl.execute(("""
						SELECT COUNT(*) FROM %s
						WHERE filename = '%s'
						""") % (db, filename))
						for row in phl:
							file_validation = row[0]

							if file_validation != 0:                                       ### the file is in the table
								found = 1
								phl.execute("""
								SELECT DISTINCT filename,createdon from %s where filename ='%s' """ % (db,filename))

								for row in phl:
										createdon = row[1]
										print  ('The file {0} was inserted in the staging table {1} the day {2}'.format(filename,db,createdon))



			if found == 0:
					print ('This file is not loaded into stage1 or stage2 tables')  ### the file is not loaded



	except:
		phl_conn.close()
		time.sleep(5)
		sys.exit(0)



