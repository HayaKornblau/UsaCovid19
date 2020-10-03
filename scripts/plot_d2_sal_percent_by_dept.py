import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce

# -------------------------------------------
# Author: Haya Kornblau
# Date  : 08/08/20 15:05
# -------------------------------------------
# Source: DeptPlot#2 - Pie Salaries by Depts
# -------------------------------------------

# init
print('\nDeptPlot No.2.. Salaries by Depts.. Start')

# fetch data
print('\nDeptPlot No.2.. Salaries by Depts.. fetch Dept..')
pd.set_option('mode.chained_assignment', None)
df_Dept = pd.read_csv('../data/tables/Dept.csv')

print('DeptPlot No.2.. Salaries by Depts.. fetch ReportDetails..')
df_ReportDetails = pd.read_csv('../data/temp/ReportDetails.csv')

print('DeptPlot No.2.. Salaries by Depts.. fetch EmpDetails..')
df_EmpDetails = pd.read_csv('../data/temp/EmpDetails.csv')

# calc
print('\nDeptPlot No.2.. Salaries by Depts.. calc..\n')
df_SalaryByDept = df_EmpDetails[['deptName'] + ['salary']]
df_SalaryByDept.to_csv('../data/temp/SalaryByDept.csv', index=False)

df_TotSalaryByDept = df_SalaryByDept.groupby(['deptName']).mean()
df_TotSalaryByDept.rename(columns={'salary': 'avgSalary'}, inplace=True)
df_TotSalaryByDept['avgSalary'] = df_TotSalaryByDept.apply((lambda x: int(x)), axis=1)  # round salaries
df_TotSalaryByDept = df_TotSalaryByDept.sort_values(by=['avgSalary'])  # sort salaries
df_TotSalaryByDept['minSalary'] = df_SalaryByDept.groupby(['deptName']).min()
df_TotSalaryByDept['maxSalary'] = df_SalaryByDept.groupby(['deptName']).max()
df_TotSalaryByDept['totSalary'] = df_SalaryByDept.groupby(['deptName']).sum()
df_TotSalaryByDept.to_csv('../data/temp/TotSalaryByDept.csv')
df_TotSalaryByDept = pd.read_csv('../data/temp/TotSalaryByDept.csv')

totalSalary = reduce((lambda x, y: x + y), df_TotSalaryByDept['totSalary'])
df_TotSalaryByDept['percentSalary'] = list(map(lambda x: x / totalSalary, df_TotSalaryByDept['totSalary']))
print(df_TotSalaryByDept)

# plot
print('\nDeptPlot No.2.. Salaries by Depts.. plotting..')
fig3, ax = plt.subplots(figsize=(7, 4.5), subplot_kw={'aspect': "equal"})
ax.axis('equal')
dept = df_TotSalaryByDept['deptName']
percentSalary = df_TotSalaryByDept['percentSalary']
colors = ['#d2d2f4', '#2b2baf', '#6464d9', '#2b2bec', '#6464d9', '#2b2bec', '#a3a3e8', '#2b2bec']
ax.pie(percentSalary, labels=dept, autopct='%1.2f%%', colors=colors)
ax.set_title("Salaries by Departments: Pie", fontsize=14)
plt.show()

# end
print('\nDeptPlot No.2.. Salaries by Depts.. Done!')
