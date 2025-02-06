'''
Written by a parent who wasn't familiar with Chicago Public Schools
Hope this helps any Chicago-area parents out there trying to figure out
what schools they should be looking at for their kids

Running this script will generate a .csv file you can open in any spreadsheet program
This repo includes a sample output file based on some criteria below

'''
import requests
import csv
import json

CPS_DATA = requests.get(
    url='https://api.cps.edu/schoolprofile/CPS/SchoolProfileCompleteData'
).json()
SCHOOL_PROFILES = CPS_DATA.get('SchoolProfile', [])
SCHOOL_PROFILES.sort(key=lambda s: s.get('Short_Name', ''))

# filter for high schools
SCHOOL_PROFILES = [S for S in SCHOOL_PROFILES if S.get('Is_High_School', 'N') == 'Y']
print(f'High Schools: {len(SCHOOL_PROFILES)}')

# filter school schools with graduation rate data
SCHOOL_PROFILES = [S for S in SCHOOL_PROFILES if S.get('Graduation_Rate_School', '') != '']
print(f'With Grad Rate Data: {len(SCHOOL_PROFILES)}')

# filter for schools with graduation rates above 80%
GRAD_RATE = 80
SCHOOL_PROFILES = [S for S in SCHOOL_PROFILES if float(S.get('Graduation_Rate_School', '0.0')) > GRAD_RATE]
print(f'Grad Rate > {GRAD_RATE}%: {len(SCHOOL_PROFILES)}')

# filter for schools with college enrollment rate data
SCHOOL_PROFILES = [S for S in SCHOOL_PROFILES if S.get('College_Enrollment_Rate_School', '') != '']
print(f'With College Enrollment Data: {len(SCHOOL_PROFILES)}')

# filter for schools with college enrollment rates above 75%
COLLEGE_ENROLLMENT_RATE = 75
SCHOOL_PROFILES = [S for S in SCHOOL_PROFILES if float(S.get('College_Enrollment_Rate_School', '0.0')) > COLLEGE_ENROLLMENT_RATE]
print(f'College Enrollment Rate > {COLLEGE_ENROLLMENT_RATE}%: {len(SCHOOL_PROFILES)}')

# filter for schools with swim programs
# (PAYTON and NORTHSIDE have Swim programs, but the CPS data doesn't show it, someone at those schools should clean up their CPS data)
SCHOOL_PROFILES = [S for S in SCHOOL_PROFILES if ('Swim' in S.get('Programs_SportsAndFitness', '') or 'PAYTON' in S.get('Short_Name', '') or 'NORTHSIDE PREP' in S.get('Short_Name', ''))]
print(f'With Swim Program: {len(SCHOOL_PROFILES)}')

with open('cps_qualifying_list.csv', 'w') as file_writer:
    csv_writer = csv.DictWriter(
        file_writer,
        fieldnames=SCHOOL_PROFILES[0].keys(),
        quoting=csv.QUOTE_ALL,
        lineterminator='\n'
    )
    csv_writer.writeheader()
    csv_writer.writerows(SCHOOL_PROFILES)

print('got here')
