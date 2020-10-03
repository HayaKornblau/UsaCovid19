import pandas as pd


# -----------------------
# Author: Haya Kornblau
# Date  : 08/08/20 17:20
# -----------------------
# Source: dept_details.py
# -----------------------

# init
print('\nDept Details.. Start')

# fetch data
print('\nManager Details.. fetching Employee, Manager..')
pd.set_option('mode.chained_assignment', None)
df_Dept = pd.read_csv('../data/tables/Dept.csv')

# print data
print('Dept Details.. printing\n')
print(df_Dept)

# end
print('\nDept Details.. Done!')
