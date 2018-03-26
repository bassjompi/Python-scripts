#!/usr/bin/python
import getpass
import pymssql
import time
import sys
import re




amg_cm_rx = ['AMG_CM_RXCLM_OPS','[AMG].[Caremark_RxClaimDetail_Stage2]']



filename = raw_input('What is the filename you would like to rollback? ')



if re.search(amg_cm_rx[0], filename):
    print('lo he encontrado')

