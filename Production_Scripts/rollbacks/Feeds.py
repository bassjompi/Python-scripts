#!/usr/bin/python



mainlist = {} ## main dictionary, each key is a filemask and contains a tupla with the feed tables




                                                ########    FEED DEFINITIONS last updated August 2017 by Juan Pablo Yanez ########


#AMERIGAS

mainlist['AMG_CM_RXCLM_OPS'] = ['[AMG].[Caremark_RxClaimDetail_Stage2]']
mainlist['AMG_HMK_PAIDMBHCLAIM']=['[AMG].[Highmark_MedicalClaimDetail_Stage2]','[AMG].[Highmark_MedicalClaimHeader_Stage2]']
mainlist['AMG_HMK_MBRSHP']=['[AMG].[Highmark_MembershipDetail_Stage2]']
mainlist['AMG_HMK_MBHUM']=['[AMG].[Highmark_UMDetail_Stage2]']



#COMCAST

###### cst/aetna
mainlist['AETNA_DAILY_ACCUM_POS_EPO']=['[Comcast].[Aetna_AccumulatorDetail_Stage1]','[Comcast].[Aetna_AccumulatorDetail_Stage2]','[Comcast].[Aetna_AccumulatorHeader]','[Comcast].[Aetna_AccumulatorTrailer]']
mainlist['COMCAST-AETNA-UM-AETNA']=['[Comcast].[Aetna_UMDetail_Stage1_BedDays]','[Comcast].[Aetna_UMDetail_Stage1_DiagnosisInfo]','[Comcast].[Aetna_UMDetail_Stage1_inpatientInfo]','[Comcast].[Aetna_UMDetail_Stage1_memberInfo]','[Comcast].[Aetna_UMDetail_Stage1_procedureInfo]','[Comcast].[Aetna_UMDetail_Stage1_Providers]','[Comcast].[Aetna_UMDetail_Stage2]','[Comcast].[Aetna_UMDetail_Stage2_DiagnosisInfo]','[Comcast].[Aetna_UMDetail_Stage2_InpatientInfo]','[Comcast].[Aetna_UMDetail_Stage2_MemberInfo]','[Comcast].[Aetna_UMDetail_Stage2_procedureInfo]','[Comcast].[Aetna_UMTrailer]']
##### cst/IBC
mainlist['STDACM_COMCAST']=['[Comcast].[IBC_AccumulatorDetail_Stage1]','[Comcast].[IBC_AccumulatorDetail_Stage2]','[Comcast].[IBC_AccumulatorHeader]','[Comcast].[IBC_AccumulatorTrailer]']
mainlist['COMCAST_BHUM310']=['[Comcast].[IBC_BHUMDetail_Stage2]']
mainlist['STDCLM_COM_CTRL']=['[Comcast].[IBC_MedicalClaimControl_Stage1]']
mainlist['STDCLM_COMCAST']=['[Comcast].[IBC_MedicalClaimDetail_Stage1]','[Comcast].[IBC_MedicalClaimDetail_Stage2]','[Comcast].[IBC_MedicalClaimHeader_Stage2]']
mainlist['STDHLD_COMCAST']=['[Comcast].[IBC_MedicalHoldCodeDetail_Stage1]','[Comcast].[IBC_MedicalHoldCodeDetail_Stage2]']
mainlist['Comcast_0']=['[Comcast].[IBC_MembershipDetail_Stage1]','[Comcast].[IBC_MembershipDetail_Stage2]']
mainlist['Comcast_1']=['[Comcast].[IBC_MembershipDetail_Stage1]','[Comcast].[IBC_MembershipDetail_Stage2]']
##### cst/magellan
mainlist['MBHACC_CLAIMSP']=['[Comcast].[Magellan_BehavioralClaimDetail_Stage2]','[Comcast].[Magellan_BehavioralClaimHeader_Stage2]']
mainlist['DATA-']=['[Comcast].[Magellan_UMDetail_Stage1]','[Comcast].[Magellan_UMDetail_Stage2]']
mainlist['CONTROL-']=['[Comcast].[Magellan_UMHeader]']
##### cst/Quest
mainlist['COMCAST-QUEST-BIOMETRIC-']=['[Comcast].[Quest_BiometricsDetail_Stage2]']
##### cst/Temple
mainlist['AC_COMCAST_CLAIMS_THP_']=['[Comcast].[Tufts_MedicalClaimDetail_Stage2]', '[Comcast].[Tufts_MedicalClaimHeader_Stage2]']
mainlist['AC_COMCAST_UM1_THP_']=['[Comcast].[Tufts_UM1Detail_Stage1]','[Comcast].[Tufts_UM1Detail_Stage2]']
mainlist['AC_COMCAST_UM1_CTOTAL_THP_']=['[Comcast].[Tufts_UM1Trailer]']
mainlist['AC_COMCAST_UM2_THP_']=['[Comcast].[Tufts_UM2Detail_Stage1]','[Comcast].[Tufts_UM2Detail_Stage2]']
mainlist['AC_COMCAST_UM2_CTOTAL_THP_']=['[Comcast].[Tufts_UM2Trailer]']
##### cst/UMR
mainlist['UMR_Comcast_Claim_']=['[Comcast].[UMR_MedicalClaimDetail_Stage2]','[Comcast].[UMR_MedicalClaimHeader_Stage2]']
mainlist['UMR_Comcast_Elig_']=['[Comcast].[UMR_MembershipDetail_Stage2]']
mainlist['CST_UMR_MBHUM_OPS_']=['[Comcast].[UMR_UMDetail_Stage2]']
##### cst/Caremark
mainlist['FILE.CNT155.COMCTAC.DT']=['[Comcast].[Caremark_RxClaimDetail_Stage1]','[Comcast].[Caremark_RxClaimDetail_Stage2]','[Comcast].[Caremark_RxClaimHeader]','[Comcast].[Caremark_RxClaimTrailer]']
##### cst/Highmark
mainlist['CST_IBC_HMK_Accum_']=['[Comcast].[Highmark_AccumulatorDetail_Stage1]','[Comcast].[Highmark_AccumulatorDetail_Stage2]','[Comcast].[Highmark_AccumulatorHeader]','[Comcast].[Highmark_AccumulatorHeader]']



#CSWG

###### cswg/aetna
mainlist['CSFC_AETNA_MBHCLM_OPS_']=['[CSWG].[Aetna_MedicalClaimDetail_Stage2]','[CSWG].[Aetna_MedicalClaimHeader_Stage2]']
mainlist['AETNA-CSFC-MBRSHP-']=['[CSWG].[Aetna_MembershipDetail_Stage2]']
mainlist['AETNA_CSFC_MUM-']=['[CSWG].[Aetna_UMDetail_Stage2]']
###### cswg/caremark
mainlist['CSFC_CM_RXCLM_']=['[CSWG].[Caremark_RxClaimDetail_Stage2]']
###### cswg/Cigna
mainlist['CSFC_CIGNA_MBHCLM_ANALYTIC_']=['[CSWG].[Cigna_MedicalClaimDetail_Stage2]','[CSWG].[Cigna_MedicalClaimHeader_Stage2]']
mainlist['CSFC_CIGNA_MBRSHP_ANALYTIC_']=['[CSWG].[Cigna_MembershipDetail_Stage2]']



#HP

###### hpe/optum
mainlist['UBH_HP_BEHAVIORAL_']=['[HP].[Optum_BHClaimsDetail_Stage1]','[HP].[Optum_BHClaimsDetail_Stage2]','[HP].[Optum_BHClaimsHeader_Stage2]']
mainlist['UHC_HP_OPTUM_RX_CLAIMS_']=['[HP].[OPTUM_RxDailyDetail_Stage1]','[HP].[OPTUM_RxDailyDetail_Stage2]','[HP].[OPTUM_RxDailyHeader]','[HP].[OPTUM_RxDailyTrailer]']
mainlist['UBH_HP_UM_']=['[HP].[Optum_UMDetail_Stage1]','[HP].[Optum_UMDetail_Stage2]','[HP].[Optum_UMHeader]','[HP].[Optum_UMTrailer]']
###### hpe/UHC
mainlist['UHC_HP_MEDICAL_']=['[HP].[UHC_MedicalClaimDetail_Stage1]','[HP].[UHC_MedicalClaimDetail_Stage2]','[HP].[UHC_MedicalClaimHeader_Stage2]']
mainlist['UHC_HP_MEMBERSHIP_']=['[HP].[UHC_MembershipBHDetail_Stage1]','[HP].[UHC_MembershipBHDetail_Stage2]','[HP].[UHC_Membershipheader]','[HP].[UHC_Membershiptrailer]','[HP].[UHC_MembershipMedicalDetail_Stage2]','[HP].[UHC_MembershipMedicalDetail_Stage1]']
mainlist['UHC_HP_RX_CLAIMS_']=['[HP].[UHC_RxDailyDetail_Stage1]','[HP].[UHC_RxDailyDetail_Stage2]','[HP].[UHC_RxDailyHeader]','[HP].[UHC_RxDailyTrailer]']
mainlist['UHC_HP_UM_']=['[HP].[UHC_UMDetail_Stage1]','[HP].[UHC_UMDetail_Stage2]','[HP].[UHC_UMHeader]','[HP].[UHC_UMTrailer]']



#IBC

mainlist['IBC_MO_MEDICALCLM_']=['[IBC].[IBC_AnalyticalMedicalClaims_Stage1]']
mainlist['IBC_ANALYTICAL_MBR_']=['[IBC].[IBC_AnalyticalMembership_Stage1]']
mainlist['IBC_MO_PHRMCLM_']=['[IBC].[IBC_AnalyticalPharmacyClaims_Stage1]']
mainlist['IBC_GRPLST_CTL_']=['[IBC].[IBC_GroupListControl_Stage1]']
mainlist['IBC_GRPLST_2']=['[IBC].[IBC_GroupListDetail_Stage1]']
mainlist['IBC_MEDICALCLM_2']=['[IBC].[IBC_MedicalClaimHeader_Stage2]','[IBC].[IBC_MedicalClaimDetail_Stage2]','[IBC].[IBC_MedicalClaimDetail_Stage1]']
mainlist['IBC_MEDICALCLM_CTL_']=['[IBC].[IBC_MedicalClaimControl_Stage1]']
mainlist['IBC_HLDCDS_']=['[IBC].[IBC_MedicalHoldCodeDetail_Stage1]','[IBC].[IBC_MedicalHoldCodeDetail_Stage2]']
mainlist['IBC_PHRMCLM_CTL_']=['[IBC].[IBC_RxDailyControl_Stage1]']
mainlist['IBC_PHRMCLM_2']=['[IBC].[IBC_RxDailyDetail_Stage1]','[IBC].[IBC_RxDailyDetail_Stage2]']
mainlist['IBC_BHUM310_']=['[IBC].[IBC_UMBHDetail_Stage2]','[IBC].[IBC_UMBHDetail_Stage1]','[IBC].[IBC_UMBHHeader]','[IBC].[IBC_UMBHTrailer]']
mainlist['IBC_UMMED_']=['[IBC].[IBC_UMDetail_Stage1]','[IBC].[IBC_UMDetail_Stage2]']



#INTUIT

##### intu/caremark
mainlist['INTU_CM_RXCLM_OPS_']=['[INTU].[Caremark_RxClaimDetail_Stage2]']
##### intu/cigna
mainlist['INTUIT_CIGNA_MBHCLM_ANALYTIC_']=['INTU.Cigna_MedicalClaimDetail_Stage2','INTU.Cigna_MedicalClaimHeader_Stage2']
##### intu/uhc
mainlist['UHC_INTU_MEDICAL_']=['[INTU].[UHC_MedicalClaimDetail_Stage2]','[INTU].[UHC_MedicalClaimHeader_Stage2]']
mainlist['UHC_INTU_MEMBERSHIP']=['[INTU].[UHC_MembershipDetail_Stage2]']
mainlist['UBH_INTU_UM_']=['[INTU].[UHC_UMBHHeader_Stage2]','[INTU].[UHC_UMBHDetail_Stage2]']
mainlist['UHC_INTU_UM_']=['[INTU].[UHC_UMDetail_Stage2]','[INTU].[UHC_UMHeader_Stage2]']



#LOWES

##### lws/bcbsal
#mainlist['BCBSAL_LOWES_MXCLAIM_PROV_HOSP']
#mainlist['BCBSAL_LOWES_MXCLAIM_REJECTED_CONTROL']
#mainlist['BCBSAL_LOWES_MXCLAIM_REJECTED_PROV_HOSP_']
#mainlist['BCBSAL_LOWES_MXCLAIM_CONTROL_']
#mainlist['BCBSAL_LOWES_MXCLAIM_MED_REJECTED_']=['[Lowes].[BCBSAL_ClaimDetail_Stage1]']
#mainlist['BCBSAL_LOWES_MXCLAIM_REJECTED_PROV_DOCT_']
#mainlist['BCBSAL_LOWES_MXCLAIM_MED_2']=['[Lowes].[BCBSAL_ClaimDetail_Stage1]']
#mainlist['BCBSAL_LOWES_MXCLAIM_PROV_DOCT_']
mainlist['BCBSAL_LOWES_ELIG_']=['[Lowes].[BCBSAL_MembershipDetail_Stage1]','[Lowes].[BCBSAL_MembershipDetail_Stage2]','[Lowes].[BCBSAL_MembershipHeader]','[Lowes].[BCBSAL_MembershipTrailer]']
mainlist['BCBSAL_LOWES_NOTES_']=['[Lowes].[BCBSAL_UMCLINICALNOTESDetail_Stage1]','[Lowes].[BCBSAL_UMCLINICALNOTESDetail_Stage2]','[Lowes].[BCBSAL_UMCLINICALNOTESHeader]','[Lowes].[BCBSAL_UMCLINICALNOTESTrailer]']
mainlist['BCBSAL_LOWES_UMDAILY_']=['[Lowes].[BCBSAL_UMDetail_Stage1]','[Lowes].[BCBSAL_UMDetail_Stage2]','[Lowes].[BCBSAL_UMHeader]','[Lowes].[BCBSAL_UMTrailer]']
mainlist['FILE.CNT155.LOWEACC.DT']=['[Lowes].[Caremark_MedicalClaimDetail_Stage2]','[Lowes].[Caremark_MedicalClaimHeader_Stage2]']
mainlist['CAREMARK_LOWES_PHARMACY_MEMBERSHIPWEEKLY_']=['[Lowes].[Caremark_MembershipDetail_Stage1]','[Lowes].[Caremark_MembershipDetail_Stage2]','[Lowes].[Caremark_Membershipheader]','[Lowes].[Caremark_MembershipTrailer]']
mainlist['FILE.CNT155.LOWESAC.DT']=['[Lowes].[Caremark_RxClaimDetail_Stage1]','[Lowes].[Caremark_RxClaimDetail_Stage2]','[Lowes].[Caremark_RxClaimHeader]','[Lowes].[Caremark_RxClaimTrailer]']



#MONSANTO

##### mons/bcbsal
mainlist['BCBSAL_MONSANTO_MXCLAIM_MED_']=['[MONS].[BCBSAL_MedicalClaimDetail_Stage2]','[MONS].[BCBSAL_MedicalClaimHeader_Stage2]']
mainlist['BCBSAL_MONSANTO_MBR_']=['[MONS].[BCBSAL_Membershipdetail_Stage2]']
mainlist['BCBSAL_MONSANTO_UMDAILY_']=['[MONS].[BCBSAL_UMDetail_Stage2]']
##### mons/ESI
mainlist['Monsanto_CDL5457_']=['[MONS].[ESI_RxClaimDetail_Stage2]']
##### mons/magellan
mainlist['MBH_MONS_CLAIMSP_']=['[MONS].[Magellan_BehavioralClaimDetail_Stage2]','[MONS].[Magellan_BehavioralClaimHeader_Stage2]']
mainlist['MAGELLAN_MONSANTO_UMDAILY_']=['[MONS].[Magellan_BHUMDetail_Stage2]']
##### mons/UHC
mainlist['UHC_MONS_MEDICAL_']=['[MONS].[UHC_MedicalClaimDetail_Stage2]','[MONS].[UHC_MedicalClaimHeader_Stage2]']
mainlist['UHC_MONS_MEMBERSHIP_']=['[MONS].[UHC_MembershipDetail_Stage2]']
mainlist['UHC_MONS_UM_']=['[MONS].[UHC_UMDetail_Stage2]','[MONS].[UHC_UMHeader_Stage2]']



#TEMPLE

##### tuhs/caremark
mainlist['CM_TUHS_RXCLM_']=['[TUHS].[Caremark_RxClaimDetail_Stage2]']
##### tuhs/IBC
mainlist['TUHS_Analy_Detail_']=['[TUHS].[IBC_AnalyticalMedicalClaims_Stage1]']
mainlist['TUHS_BHUM310_']=['[TUHS].[IBC_BHUMDetail_Stage2]']
mainlist['STDCLM_TUHS_']=['[TUHS].[IBC_MedicalClaimDetail_Stage2]','[TUHS].[IBC_MedicalClaimHeader_Stage2]']
mainlist['TUHS_0']=['[TUHS].[IBC_MembershipDetail_Stage2]']
mainlist['TUHS_PreCert_Report_']=['[TUHS].[IBC_UMDetail_Stage2]']

