#!/usr/bin/python

import getpass
import pymssql
from rollbacks.Feeds import *

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
encrypt= '%txt'
pattern ='Stage1'

for filemask in mainlist:

	for db in mainlist[filemask]:
             print ('testing db {}'.format(db))
             phl.execute(("""
		     select count(*) filename from %s where filename like '%s'
		     """) % (db, encrypt))

             print ('ok')


print ('\nTest is finished')
phl = phl_conn.close()