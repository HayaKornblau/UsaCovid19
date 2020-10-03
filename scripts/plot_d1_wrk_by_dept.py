import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------
# Author: Haya Kornblau
# Date  : 08/08/20 15:00
# ----------------------------------------
# Source: DeptPlot#1 - Work Days by Depts
# ----------------------------------------

# init
print('\nDeptPlot No.1.. Work Days by Depts.. Start')

# fetch data
print('\nDeptPlot No.1.. Work Days by depts.. fetch Dept..')
pd.set_option('mode.chained_assignment', None)
df_Dept = pd.read_csv('../data/tables/Dept.csv')

print('DeptPlot No.1.. Work Days by depts.. fetch TotReportByDateType..\n')
df_TotReportByDateType = pd.read_csv('../data/temp/TotReportByDateType.csv')
cols = list(df_TotReportByDateType.columns)
print(cols)
print(df_TotReportByDateType)

# calc data
print('\nDeptPlot No.1.. Work Days by depts.. calc..\n')
df_WrkDaysByDept = df_TotReportByDateType[['date']]

for deptName in df_Dept['deptName']:
    df_WrkDaysByDept['wrkDays' + deptName] = df_TotReportByDateType.apply(lambda x1: x1['wrkDays' + deptName], axis=1)

df_WrkDaysByDept.to_csv('../data/temp/WrkDaysByDept.csv', index=False)
df_WrkDaysByDept = pd.read_csv('../data/temp/WrkDaysByDept.csv')
print(df_WrkDaysByDept)

# plot
print('\nDeptPlot No.1.. Work Days by Depts.. plotting..\n')
cols = list(df_WrkDaysByDept.columns)
dates = df_WrkDaysByDept.date
wrkDaysHlt = df_WrkDaysByDept.wrkDaysHealth
wrkDaysMng = df_WrkDaysByDept.wrkDaysManagement
wrkDaysSnt = df_WrkDaysByDept.wrkDaysSenat

x = np.arange(len(dates))
plt.bar(x - 0.25, wrkDaysHlt, label='Health', color='#FA8072', width=0.25)
plt.bar(x + 0.00, wrkDaysMng, label='Management', color='#E23D28', width=0.25)
plt.bar(x + 0.25, wrkDaysSnt, label='Senat', color='#7C0A02', width=0.25)

plt.title('Work Days by Departements', fontsize=14)
plt.margins(.12, .12)
plt.ylabel('Amount of Days')
plt.xticks(x, dates, fontsize=8, rotation=25, ha='right')
plt.legend(loc='best')
plt.show()

# end
print('\nDeptPlot No.1.. Work Days by Depts.. Done!')
