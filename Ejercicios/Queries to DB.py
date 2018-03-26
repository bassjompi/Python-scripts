#!/usr/bin/python

import getpass
import pymssql
import time
import sys

from pip.commands.list import tabulate

print ('Rollback tool from stage 1 and stage 2 - Accolade')
print ('Juan Pablo Yanez Camacho - Aug. 2017 - v0.1')
print

phl_server = "PHL-DAQ"


username = raw_input('Please enter your username: ')
user = 'ACCPROD1\%s' % username
password = getpass.getpass()

while True :
	try :
		print ("Connecting to DB's....")
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

while True :
	print ('Please choose customer')
	print ('0. Exit')
	print ('1. Amerigas')
	print ('2. Comcast')
	print ('3. CSWG')
	print ('4. HP')
	print ('5. IBC')
	print ('6. Intuit')
	print ('7. Lowes')
	print ('8. Monsanto')
	print ('9. Temple')


	customer = input()

	if customer == 0:
		phl = phl_conn.close()
		sys.exit(0)


	print ('please choose data partner')

	if customer == 1:  #Data partners for AMG customer
		print ('0. Cancel')
		print ('1. Caremark')
		print ('2. Highmark')

	elif customer == 2:   #Data partners for CST customer
		print ('0. Cancel')
		print ('1. Aetna')
		print ('2. IBC')
		print ('3. Magellan')
		print ('4. Quest')
		print ('5. Temple')
		print ('6. UMR')
		print ('7. Caremark')
		print ('8. Highmark')

	elif customer == 3:  # Data partners for CSWG customer
		print ('0. Cancel')
		print ('1. Aetna')
		print ('2. Caremark')
		print ('3. Cigna')

	elif customer == 4:  # Data partners for HP customer
		print ('0. Cancel')
		print ('1. Optum')
		print ('2. UHC')

	elif customer == 5:  # Data partners for IBC customer
		print ('0. Cancel')
		print ('1. IBC')

	elif customer == 6:  # Data partners for Intuit customer
		print ('0. Cancel')
		print ('1. Caremark')
		print ('2. Cigna')
		print ('3. UHC')

	elif customer == 7:  # Data partners for Lowes customer
		print ('0. Cancel')
		print ('1. BCBSAL')
		print ('2. Caremark')

	elif customer == 8:  # Data partners for Monsanto customer
		print ('0. Cancel')
		print ('1. BCBSAL')
		print ('2. Magellan')
		print ('3. UHC')

	elif customer == 9:  # Data partners for TUHS customer
		print ('0. Cancel')
		print ('1. IBC')
		print ('2. Caremark')


	else:
		print('please spcify a valid option')

	Partner = input()


	if Partner == 0:
		phl = phl_conn.close()
		sys.exit(0)

	print ('\nplease choose feed type')


##### AMERIGAS  ######################################################
	if customer == 1  and Partner == 1:
		print ('0. Cancel')
		print ('1. Pharmacy Claims')

	if customer == 1  and Partner == 2:
		print ('0. Cancel')
		print ('1. Medical Clains')
		print ('2. Membership')
		print ('3. UM')


##########  COMCAST   ################################################

	if customer == 2  and Partner == 1:
		print ('0. Cancel')
		print ('1. Accumulator')
		print ('2. UM')

	if customer == 2  and Partner == 2:
		print ('0. Cancel')
		print ('1. Accumulator')
		print ('2. BHUM')
		print ('3. Medical Claims')
		print ('4. Medical Holdcodes')
		print ('5. Membership')

	if customer == 2  and Partner == 3:
		print ('0. Cancel')
		print ('1. Behavioural Claims')
		print ('2. UM')

	if customer == 2  and Partner == 4:
		print ('0. Cancel')
		print ('1. Biometric details')

	if customer == 2  and Partner == 5:
		print ('0. Cancel')
		print ('1. Medical claims')
		print ('2. UM')

	if customer == 2  and Partner == 6:
		print ('0. Cancel')
		print ('1. Medical claims')
		print ('2. UM')
		print ('3. Membership')

	if customer == 2  and Partner == 7:
		print ('0. Cancel')
		print ('1. Pharmacy Claims')

	if customer == 2  and Partner == 8:
		print ('0. Cancel')
		print ('1. Accumulator')


####  CSWG  ########################################################

	if customer == 3 and Partner == 1:
		print ('0. Cancel')
		print ('1. Medical Claims')
		print ('2. Membership')
		print ('3. UM')

	if customer == 3  and Partner == 2:
		print ('0. Cancel')
		print ('1. Pharmacy Claims')

	if customer == 3 and Partner == 3:
		print ('0. Cancel')
		print ('1. Medical Claims')
		print ('2. Membership')


######   HP    #######################################################

	if customer == 4 and Partner == 1:
		print ('0. Cancel')
		print ('1. Behavioural Claims')
		print ('2. Pharmacy claims')
		print ('3. UM')

	if customer == 4  and Partner == 2:
		print ('0. Cancel')
		print ('1. Medical Claims')
		print ('2. Membership')
		print ('3. Pharmacy claims')
		print ('4. UM')


######    IBC   ########################################################

	if customer ==5:
		print ('0. Cancel')
		print ('1. Analytical Medical Claims')
		print ('2. Analytical Pharmacy Claims')
		print ('3. Group List')
		print ('4. Medical Claims')
		print ('5. Medical Hold codes')
		print ('6. Pharmacy claims')
		print ('7. Behavioural UM')
		print ('8. UM')


######   INTU    #######################################################

	if customer == 6 and Partner == 1:
			print ('0. Cancel')
			print ('1. Pharmacy claims')

	if customer == 6 and Partner == 2:
			print ('0. Cancel')
			print ('1. Medical Claims')

	if customer == 6 and Partner == 3:
			print ('0. Cancel')
			print ('1. Medical Claims')
			print ('2. Membership')
			print ('3. Behavioural UM')
			print ('4. UM')



	######   LOWES    #######################################################


	if customer == 7 and Partner == 1:
		print ('0. Cancel')
		print ('1. Analytical Medical Claims')
		print ('2. Medical Claims')
		print ('3. Membership')
		print ('4. UM')
		print ('5. Clinical notes')

	if customer == 7 and Partner == 2:
		print ('0. Cancel')
		print ('1. Medical Claims')
		print ('2. Membership')
		print ('3. Pharmacy claims')




######   MONSANTO    #######################################################


	if customer == 8 and Partner == 1:
		print ('0. Cancel')
		print ('1. Medical Claims')
		print ('2. Membership')
		print ('3. UM')


	if customer == 8 and Partner == 2:
		print ('0. Cancel')
		print ('1. Behavioural claims')
		print ('2. Behavioural UM')

	if customer == 8 and Partner == 3:
		print ('0. Cancel')
		print ('1. Medical Claims')
		print ('2. Membership')
		print ('3. UM')



######   MONSANTO    #######################################################

	if customer == 9 and Partner == 1:
		print ('0. Cancel')
		print ('1. Behavioural UM')
		print ('2. Medical Claims')
		print ('3. Membership')
		print ('4. UM')

	if customer == 9 and Partner == 2:
		print ('0. Cancel')
		print ('1. Pharmacy claims')


	feed = input()
	if feed == 0:
		phl = phl_conn.close()
		sys.exit(0)


	database = (customer,Partner,feed)
	filename = raw_input('What is the filename you would like to rollback? ')
	print ("You will rollback all date on stage1 and stage2 tables for the file with name: '%s' ") % (filename)



	if database == (1,1,1):
		table = ['[AMG].[Caremark_RxClaimDetail_Stage2]']  #AMG  CM  RX

	elif database == (1,2,1):
		table = ['[AMG].[Highmark_MedicalClaimDetail_Stage2]','[AMG].[Highmark_MedicalClaimHeader_Stage2]']  # AMG HMK MEDCLM

	elif database == (1,2,2):
		table = ['[AMG].[Highmark_MembershipDetail_Stage2]']   # AMG HMK MEMBERSHIP

	elif database == (1,2,3):
		table = ['[AMG].[Highmark_UMDetail_Stage2]']   #AMG HMK UM




	elif database == (2,1,1):
		table = ['[Comcast].[Aetna_AccumulatorDetail_Stage1]','[Comcast].[Aetna_AccumulatorDetail_Stage2]','[Comcast].[Aetna_AccumulatorDetail_Stage2_Type]','[Comcast].[Aetna_AccumulatorHeader]','[Comcast].[Aetna_AccumulatorTrailer]']

	elif database == (2,1,2):
		table = ['[Comcast].[Aetna_UMDetail_Stage1_BedDays]','[Comcast].[Aetna_UMDetail_Stage1_DiagnosisInfo]','[Comcast].[Aetna_UMDetail_Stage1_inpatientInfo]','[Comcast].[Aetna_UMDetail_Stage1_memberInfo]','[Comcast].[Aetna_UMDetail_Stage1_procedureInfo]','[Comcast].[Aetna_UMDetail_Stage1_Providers]','[Comcast].[Aetna_UMDetail_Stage2]','[Comcast].[Aetna_UMDetail_Stage2_DiagnosisInfo]','[Comcast].[Aetna_UMDetail_Stage2_InpatientInfo]','[Comcast].[Aetna_UMDetail_Stage2_MemberInfo]','[Comcast].[Aetna_UMDetail_Stage2_procedureInfo]','[Comcast].[Aetna_UMTrailer]']

	elif database == (2, 2, 1):
		table = ['[Comcast].[IBC_AccumulatorDetail_Stage1]','[Comcast].[IBC_AccumulatorDetail_Stage2]','[Comcast].[IBC_AccumulatorHeader]','[Comcast].[IBC_AccumulatorTrailer]']

	elif database == (2, 2, 2):
		table = ['[Comcast].[IBC_BHUMDetail_Stage2]']

	elif database == (2,2,3):
		table = ['[Comcast].[IBC_MedicalClaimControl_Stage1]','[Comcast].[IBC_MedicalClaimDetail_Stage1]','[Comcast].[IBC_MedicalClaimDetail_Stage2]','[Comcast].[IBC_MedicalClaimHeader_Stage2]']

	elif database == (2,2,4):
		table = ['[Comcast].[IBC_MedicalHoldCodeDetail_Stage1]','[Comcast].[IBC_MedicalHoldCodeDetail_Stage2]']

	elif database == (2,2,5):
		table = ['[Comcast].[IBC_MembershipDetail_Stage1]','[Comcast].[IBC_MembershipDetail_Stage2]']

	elif database == (2,3,1):
		table = ['[Comcast].[Magellan_BehavioralClaimDetail_Stage2]','[Comcast].[Magellan_BehavioralClaimHeader_Stage2]']

	elif database == (2,3,2):
		table = ['[Comcast].[Magellan_UMDetail_Stage1]','[Comcast].[Magellan_UMDetail_Stage2]','[Comcast].[Magellan_UMHeader]']

	elif database == (2,4,1):
		table = ['[Comcast].[Quest_BiometricsDetail_Stage2]']

	elif database == (2,5,1):
		table = ['[Comcast].[Tufts_MedicalClaimDetail_Stage2]', '[Comcast].[Tufts_MedicalClaimHeader_Stage2]']

	elif database == (2,5,2):
		table = ['[Comcast].[Tufts_UM1Detail_Stage1]','[Comcast].[Tufts_UM1Detail_Stage2]','[Comcast].[Tufts_UM1Trailer]','[Comcast].[Tufts_UM2Detail_Stage1]','[Comcast].[Tufts_UM2Detail_Stage2]','[Comcast].[Tufts_UM2Trailer]']

	elif database == (2,6,1):
		table = ['[UMR_MedicalClaimDetail_Stage2]','[UMR_MedicalClaimHeader_Stage2]']

	elif database == (2, 6, 2):
		table = ['[Comcast].[UMR_UMDetail_Stage2]']

	elif database == (2, 6, 3):
		table = ['[Comcast].[UMR_MembershipDetail_Stage2]']

	elif database == (2,7,1):
		table = ['[DAQ_STG].[Comcast].[Caremark_RxClaimDetail_Stage1]','[Comcast].[Caremark_RxClaimDetail_Stage2]','[Comcast].[Caremark_RxClaimHeader]','[Comcast].[Caremark_RxClaimTrailer]']

	elif database == (2,8,1):
		table = ['[Comcast].[Highmark_AccumulatorDetail_Stage1]','[Comcast].[Highmark_AccumulatorDetail_Stage2]','[Comcast].[Highmark_AccumulatorHeader]','[Comcast].[Highmark_AccumulatorHeader]']




	elif database == (3,1,1):
		table = ['[CSWG].[Aetna_MedicalClaimDetail_Stage2]','[CSWG].[Aetna_MedicalClaimHeader_Stage2]']

	elif database == (3,1,2):
		table = ['[CSWG].[Aetna_MembershipDetail_Stage2]']

	elif database == (3, 1, 3):
		table = ['[CSWG].[Aetna_UMDetail_Stage2]']

	elif database == (3, 2, 1):
		table = ['[CSWG].[Caremark_RxClaimDetail_Stage2]']

	elif database == (3, 3, 1):
		table = ['[CSWG].[Cigna_MedicalClaimDetail_Stage2]','[CSWG].[Cigna_MedicalClaimHeader_Stage2]']

	elif database == (3, 3, 2):
		table = ['[CSWG].[Cigna_MembershipDetail_Stage2]']




	elif database == (4, 1, 1):
		table = ['[HP].[Optum_BHClaimsDetail_Stage1]','[HP].[Optum_BHClaimsDetail_Stage2]','[HP].[Optum_BHClaimsHeader_Stage2]']

	elif database == (4, 1, 2):
		table = ['[HP].[OPTUM_RxDailyDetail_Stage1]','[HP].[OPTUM_RxDailyDetail_Stage2]','[HP].[OPTUM_RxDailyHeader]','[HP].[OPTUM_RxDailyTrailer]']

	elif database == (4, 1, 3):
		table = ['[HP].[Optum_UMDetail_Stage1]','[HP].[Optum_UMDetail_Stage2]','[HP].[Optum_UMHeader]','[HP].[Optum_UMTrailer']

	elif database == (4, 2, 1):
		table = ['[HP].[UHC_MedicalClaimDetail_Stage1]','[HP].[UHC_MedicalClaimDetail_Stage2]','[HP].[UHC_MedicalClaimHeader_Stage2]']

	elif database == (4, 2, 2):
		table = ['[HP].[UHC_MembershipBHDetail_Stage1]','[HP].[UHC_MembershipBHDetail_Stage2]','[HP].[UHC_Membershipheader]','[HP].[UHC_Membershiptrailer]','[HP].[UHC_MembershipMedicalDetail_Stage2]','[HP].[UHC_MembershipMedicalDetail_Stage1]']

	elif database == (4, 2, 3):
		table = ['[HP].[UHC_RxDailyDetail_Stage1]','[HP].[UHC_RxDailyDetail_Stage2]','[HP].[UHC_RxDailyHeader]','[HP].[UHC_RxDailyTrailer]']

	elif database == (4, 2, 4):
		table = ['[HP].[UHC_UMDetail_Stage1]','[HP].[UHC_UMDetail_Stage2]','[HP].[UHC_UMHeader]','[HP].[UHC_UMTrailer]']





	elif database == (5, 1, 1):



	for element in table:
		#print (element)
		phl.execute(("""select distinct filename from %s """) % element)
		result = phl.fetchall()
		print tabulate(result)


	phl = phl_conn.close()
	sys.exit(0)
