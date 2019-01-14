# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:32:49 2019

@author: anurag
"""

import csv
f1 = open ("Accidents.csv","r") # open input file for reading 
users_dict = {}
with open('out.csv', 'w') as f: # output csv file
   # writer = csv.writer(f)
    headers = ['CAL_YR', 'CAL_QTR', 'ACCIDENT_TIME', 'DEGREE_INJURY_CD', 'DEGREE_INJURY', 'FIPS_STATE_CD', 'UG_LOCATION_CD', 'UG_LOCATION',	'UG_MINING_METHOD_CD', 'UG_MINING_METHOD', 'MINING_EQUIP_CD	', 'MINING_EQUIP', 'EQUIP_MFR_CD', 'EQUIP_MFR_NAME',	 'EQUIP_MODEL_NO', 'SHIFT_BEGIN_TIME', 'CLASSIFICATION_CD', 'CLASSIFICATION',	'ACCIDENT_TYPE_CD',	'ACCIDENT_TYPE',	'NO_INJURIES',	'TOT_EXPER',	'MINE_EXPER', 'JOB_EXPER',	'OCCUPATION_CD', 'OCCUPATION',	'ACTIVITY_CD', 'ACTIVITY',	'INJURY_SOURCE_CD',	'INJURY_SOURCE',	'NATURE_INJURY_CD',	'NATURE_INJURY',	'INJ_BODY_PART_CD',	'INJ_BODY_PART',	'SCHEDULE_CHARGE',	 'DAYS_RESTRICT',	'DAYS_LOST',	'TRANS_TERM',	'IMMED_NOTIFY_CD',	 'IMMED_NOTIFY', 'NARRATIVE', 'COAL_METAL_IND']
    writer = csv.DictWriter(f, lineterminator='\n', delimiter=',', fieldnames=headers)
    writer.writeheader()
    with open('Accidents.csv','r') as csvfile: # input csv file
        reader = csv.DictReader(csvfile, delimiter=',')
        a = 1
        for row in reader:
            #print (row['Claim Injury Type'], row['Age at Injury'], row['WCIO Part Of Body Code'], row['WCIO Nature of Injury Code'], row['WCIO Cause of Injury Code'], row['Gender'])
            #users_dict.update(row)
            cur = [row['CAL_YR'], row['CAL_QTR'], row['ACCIDENT_TIME'], row['DEGREE_INJURY_CD'], row['DEGREE_INJURY'], row['FIPS_STATE_CD'], row['UG_LOCATION_CD'], row['UG_LOCATION'], row['UG_MINING_METHOD_CD'], row['UG_MINING_METHOD'], row['MINING_EQUIP_CD'], row['MINING_EQUIP'], row['EQUIP_MFR_CD'], row['EQUIP_MFR_NAME'], row['EQUIP_MODEL_NO'], row['SHIFT_BEGIN_TIME'], row['CLASSIFICATION_CD'], row['CLASSIFICATION'], row['ACCIDENT_TYPE_CD'], row['ACCIDENT_TYPE'], row['NO_INJURIES'], row['TOT_EXPER'], row['MINE_EXPER'], row['JOB_EXPER'], row['OCCUPATION_CD'], row['OCCUPATION'], row['ACTIVITY_CD'], row['ACTIVITY'], row['INJURY_SOURCE_CD'], row['INJURY_SOURCE'], row['NATURE_INJURY_CD'], row['NATURE_INJURY'], row['INJ_BODY_PART_CD'], row['INJ_BODY_PART'], row['SCHEDULE_CHARGE'], row['DAYS_RESTRICT'], row['DAYS_LOST'], row['TRANS_TERM'], row['IMMED_NOTIFY_CD'], row['IMMED_NOTIFY'], row['NARRATIVE'], row['COAL_METAL_IND']]
            i = 0
            restart = False
            for ele in cur:
# =============================================================================
#                 if(ele == 'UK'):
#                     restart = True
#                     break
# =============================================================================
                users_dict[headers[i]] = ele
                i = i + 1
            if restart == True:
                continue
            #print(users_dict)    
            writer.writerow(users_dict)

f1.close()