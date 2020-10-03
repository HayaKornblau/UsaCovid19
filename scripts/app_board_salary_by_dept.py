import pandas as pd
from functools import reduce

# ---------------------
# Author: Haya Kornblau
# Date:  17/05/20 02:10
# ----------------------

# init
print('\nBoard of Salaries by Dept.. Start')

# fetch Data
pd.set_option('mode.chained_assignment', None)
df_Dept = pd.read_csv('../data/tables/Dept.csv')
df_EmpDetails = pd.read_csv('../data/temp/EmpDetails.csv')
df_ReportDetails = pd.read_csv('../data/temp/ReportDetails.csv')

# filter data by dept
df_SalaryByDept = df_EmpDetails[['deptName'] + ['salary']]
df_SalaryByDept.to_csv('../data/temp/SalaryByDept.csv', index=False)

# calc salaries statistics by dept
print('\nBoard of Salaries by Dept ..Statistics start')
df_TotSalaryByDept = df_SalaryByDept.groupby(['deptName']).mean()
df_TotSalaryByDept.rename(columns={'salary': 'avgSalary'}, inplace=True)
df_TotSalaryByDept['avgSalary'] = df_TotSalaryByDept.apply((lambda x: int(x)), axis=1)  # round salaries
df_TotSalaryByDept = df_TotSalaryByDept.sort_values(by=['avgSalary'])  # sort by avgSalary
df_TotSalaryByDept['minSalary'] = df_SalaryByDept.groupby(['deptName']).min()
df_TotSalaryByDept['maxSalary'] = df_SalaryByDept.groupby(['deptName']).max()
df_TotSalaryByDept['totSalary'] = df_SalaryByDept.groupby(['deptName']).sum()
df_TotSalaryByDept.to_csv('../data/temp/TotSalaryByDept.csv')
df_TotSalaryByDept = pd.read_csv('../data/temp/TotSalaryByDept.csv')

# calc salaries percents for pie plotting
totalSalary = reduce((lambda x, y: x + y), df_TotSalaryByDept['totSalary'])
df_TotSalaryByDept['percentSalary'] = list(map(lambda x: x / totalSalary, df_TotSalaryByDept['totSalary']))
print('Board of Salaries by Dept ..Statistics end\n')

# list of salaries by emp
df_EmployeeTmp = df_EmpDetails[['empId'] + ['firstName'] + ['lastName'] + ['deptName'] + ['salary']]
print('List of Employee Salaries..\n')
print(df_EmployeeTmp)

# get salary range
fromSalary = int(input('\nPlease enter low range of salary: '))
toSalary = int(input('Please enter high range of salary: '))

# query
df_query = \
    df_EmployeeTmp[(df_EmployeeTmp['salary'] >= fromSalary) &
                   (df_EmployeeTmp['salary'] <= toSalary)].sort_values(by=['salary'])

# print results
print('\nBoard of Salaries by Dept.. Results\n')
print(df_query)

# save data to file
saveToFileInput = input('\nSave report (Y/N)? ')
saveFlag = saveToFileInput.upper() == 'Y'

if saveFlag:
    saveToFile = input("\nEnter file the name of your text file - please use / backslash when typing path: ")
    # C:/Users/User/source/repos/PyProjs/UsaCovid19/docs/SalaryByDept_160520_1336.csv

    # save report
    print('\nBoard of Salaries by Dept.. save to file..')
    df_query.to_csv(saveToFile, index=False)

# end board
print('\nBoard of Salaries by Dept.. Done!\n')
