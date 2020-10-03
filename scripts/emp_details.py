import pandas as pd

# ----------------------
# Author: Haya Kornblau
# Date: 04/08/20 14:00
# ----------------------

# init
print('\nPrinting Employee Details.. Start')

# fetch Employee, Dept, Position, Manager data
print('\nFetching Employee, Dept, Position data..')
pd.set_option('mode.chained_assignment', None)
df_Emp = pd.read_csv('../data/tables/Employee.csv')
df_Dept = pd.read_csv('../data/tables/Dept.csv')
df_Position = pd.read_csv('../data/tables/Position.csv')
df_Manager = pd.read_csv('../data/tables/Manager.csv')

# merge Dept, Position data
print('Merging Dept, Position data..')
df_EmpDetails = pd.merge(df_Emp, df_Dept, on='deptId')
df_EmpDetails = pd.merge(df_EmpDetails, df_Position, on='positionId')

# merge Manager
print('Merging Manager data..')
df_EmpDetails = pd.merge(df_EmpDetails, df_Manager, how='left', on='empId')
df_EmpDetails = pd.merge(df_EmpDetails, df_Emp, how='left',
                         left_on='managerId', right_on='empId', suffixes=('', '_Manager'))
cols = list(df_EmpDetails.columns)
df_EmpDetails.rename(columns={'firstName_Manager': 'managerFirstName',
                              'lastName_Manager': 'managerLastName'}, inplace=True)

df_EmpDetails = df_EmpDetails.filter(['empId', 'firstName', 'lastName', 'gender', 'birthDate', 'deptName',
                                      'positionName', 'managerFirstName', 'managerLastName', 'salary'])

# save & print
df_EmpDetails.to_csv('../data/temp/EmpDetails.csv', index=False)
print('\nPrinting Employee Details..\n')
print(df_EmpDetails)
print('\nEmployee Details.. Done!')
