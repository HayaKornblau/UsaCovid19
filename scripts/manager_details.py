import pandas as pd

# ----------------------
# Author: Haya Kornblau
# Date: 14/05/20 21:35
# ----------------------

# init
print('\nManager Details.. Start')

# fetch data
print('\nManager Details.. fetching Employee, Manager..')
pd.set_option('mode.chained_assignment', None)
df_Emp = pd.read_csv('../data/tables/Employee.csv')
df_Manager = pd.read_csv('../data/tables/Manager.csv')

# merge Emp, Manager
print('Manager Details.. merging Manager data..')
df_ManagerDetails = pd.merge(df_Emp, df_Manager, how='left', on='empId')
df_ManagerDetails = pd.merge(df_ManagerDetails, df_Emp, how='left',
                             left_on='managerId', right_on='empId', suffixes=('', '_Manager'))
cols = list(df_ManagerDetails.columns)
df_ManagerDetails.rename(columns={'firstName_Manager': 'managerFirstName',
                                  'lastName_Manager': 'managerLastName'}, inplace=True)
df_ManagerDetails = df_ManagerDetails.filter(['empId', 'firstName', 'lastName',
                                              'managerId', 'managerFirstName', 'managerLastName'])
df_ManagerDetails.to_csv('../data/temp/ManagerDetails.csv', index=False)

# print
print('\nManager Details.. printing\n')
print(df_ManagerDetails)

# end
print('\nManager Details.. Done!')
