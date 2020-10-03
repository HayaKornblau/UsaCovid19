import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------
# Author: Haya Kornblau
# Date  : 29/08/20 14:50
# ------------------------------------------------
# Source: DeptPlot#3 - Salary Statistics by Depts
# ------------------------------------------------

# init
print('\nDeptPlot No.3.. Salary Statistics by Dept.. Start')

# fetch data
print('\nDeptPlot No.3.. Salary Statistics by Dept.. fetch ReportDetails..')
pd.set_option('mode.chained_assignment', None)
df_ReportDetails = pd.read_csv('../data/temp/ReportDetails.csv')

print('DeptPlot No.3.. Salary Statistics by Dept.. fetch EmpDetails..')
df_EmpDetails = pd.read_csv('../data/temp/EmpDetails.csv')

# calc
print('\nDeptPlot No.3.. Salary Statistics by Dept.. calc..\n')
df_SalaryByDept = df_EmpDetails[['deptName'] + ['salary']]
df_SalaryByDept.to_csv('../data/temp/SalaryByDept.csv', index=False)

df_TotSalaryByDept = df_SalaryByDept.groupby(['deptName']).mean()
df_TotSalaryByDept.rename(columns={'salary': 'avgSalary'}, inplace=True)
df_TotSalaryByDept['avgSalary'] = df_TotSalaryByDept.apply((lambda x: int(x)), axis=1)
df_TotSalaryByDept = df_TotSalaryByDept.sort_values(by=['avgSalary'])
df_TotSalaryByDept['minSalary'] = df_SalaryByDept.groupby(['deptName']).min()
df_SalaryByDept.groupby(['deptName']).min()
df_TotSalaryByDept['maxSalary'] = df_SalaryByDept.groupby(['deptName']).max()
df_TotSalaryByDept['totSalary'] = df_SalaryByDept.groupby(['deptName']).sum()
df_TotSalaryByDept.to_csv('../data/temp/TotSalaryByDept.csv')
df_TotSalaryByDept = pd.read_csv('../data/temp/TotSalaryByDept.csv')
print(df_TotSalaryByDept)

# plot
print('\nDeptPlot No.3.. Salary Statistics by Dept.. plotting...')
dept = df_TotSalaryByDept['deptName']
avgSalaryList = df_TotSalaryByDept['avgSalary']
minSalaryList = df_TotSalaryByDept['minSalary']
maxSalaryList = df_TotSalaryByDept['maxSalary']

fig2, ax = plt.subplots()
ax.plot(dept, maxSalaryList, '#2F4F4F', label='max', linewidth=2.4)
ax.plot(dept, avgSalaryList, '#778899', label='avg', linewidth=2.4)
ax.plot(dept, minSalaryList, '#A9A9A9', label='min', linewidth=2.4)

plt.title('Salaries by Departments', fontsize=14)
plt.margins(.12, .12)
plt.ylabel('Amount of Salary')
maxSalary = max(maxSalaryList)
plt.yticks(np.arange(0, maxSalary * 1.1, 20000))
plt.legend(loc='best')
plt.show()

# end
print('\nDeptPlot no.3.. Salary Statistics by Dept.. Done!')
