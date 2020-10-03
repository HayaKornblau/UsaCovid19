import pandas as pd

# ----------------------
# Author: Haya Kornblau
# Date:  18/05/20 17:00
# ----------------------

print('Board by Employee.. Start\n')

pd.set_option('mode.chained_assignment', None)
df_EmpDetails = pd.read_csv('../data/temp/EmpDetails.csv')
print(df_EmpDetails)

# get emp
empType = input('Please enter employee input type, or leave empty for select all (1-Id, 2-Name): ')

if empType == '1':
    empId = int(input('Please enter Employee Id: '))
    df_query = df_EmpDetails[df_EmpDetails.empId == empId]

elif empType == '2':
    firstName = input('Please enter employee\'s first name: ')
    print(type(firstName))
    lastName = input('Please enter employee\'s last name: ')
    df_query = \
        df_EmpDetails[(df_EmpDetails['firstName'] == firstName) & (df_EmpDetails['lastName'] == lastName)]

else:
    df_query = df_EmpDetails

# print emp details
print(df_query)

# save data to file
saveToFileInput = input('\nSave report (Y/N)? ')
saveFlag = saveToFileInput in ('Y', 'y')

if saveFlag:
    saveToFile = input("\nEnter file the name of your text file - please use / backslash when typing path: ")
    # C:/Users/User/Documents/BR/empQuery_160520_1336.csv

    print('\nBoard by Employee.. save to file..10')
    df_query.to_csv(saveToFile, index=False)

# end board
print('\nBoard by Employee.. Done!\n')
