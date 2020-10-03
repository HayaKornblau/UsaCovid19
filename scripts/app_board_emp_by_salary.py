import pandas as pd

# ----------------------
# Author: Haya Kornblau
# Date:  17/05/20 02:10
# ----------------------

# init
print('\nBoard of Employee Salaries by Range.. Start')

# fetch Data
pd.set_option('mode.chained_assignment', None)
df_Employee = pd.read_csv('../data/tables/Employee.csv')
df_EmployeeTmp = df_Employee[['empId'] + ['firstName'] + ['lastName'] + ['salary']]
print('\nList of Employee Salaries..\n')
print(df_EmployeeTmp)

# get salaries range
fromSalary = int(input('\nPlease enter low range of salary: '))
toSalary = int(input('Please enter high range of salary: '))

# query
df_query = \
    df_EmployeeTmp[(df_EmployeeTmp['salary'] >= fromSalary) &
                   (df_EmployeeTmp['salary'] <= toSalary)].sort_values(by=['salary'])

# print results
print('\nBoard of Employee Salaries by Range.. Results\n')
print(df_query)

# save data to file
saveToFileInput = input('\nSave report (Y/N)? ')
saveFlag = saveToFileInput.upper() == 'Y'

if saveFlag:
    saveToFile = input("\nEnter file the name of your text file - please use / backslash when typing path: ")
    # C:/Users/User/source/repos/PyProjs/UsaCovid19/docs/EmpBySalary_160520_1336.csv

    # save
    print('\nBoard of Employee Salaries by Range.. save to file..')
    df_query.to_csv(saveToFile, index=False)

# end board
print('\nBoard of Employee Salaries by Range.. Done!\n')
