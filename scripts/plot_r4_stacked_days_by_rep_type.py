import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# Author: Haya Kornblau
# Date  : 08/08/20 17:30
# --------------------------------------------------
# Source: WorkPlot#4 - Total Days by Reporting Type
# --------------------------------------------------

# init
print('\nWork Plot No.4.. Total Days by Reporting Type.. Start')

# fetch data
print('\nWork Plot No.4.. Total Days by Reporting Type.. fetch TotReportByDateType..\n')
df_TotDaysByDate = pd.read_csv('../data/temp/TotReportByDateType.csv')
print(df_TotDaysByDate)

# plot
print('\nWork Plot No.4..Total Days by Reporting Type.. plotting..')
dates = df_TotDaysByDate.date
x = np.arange(len(dates))
wrkDays = df_TotDaysByDate.wrkDays
vacDays = df_TotDaysByDate.vacDays
sckDays = df_TotDaysByDate.sckDays

# Heights of Work + Vacation
daysWrkVac = np.add(wrkDays, vacDays).tolist()

plt.bar(dates, wrkDays, label='Work Days', color='b', width=0.5)
plt.bar(dates, vacDays, label='Vacation', bottom=wrkDays, color='y', width=0.5)
plt.bar(dates, sckDays, label='Sick', bottom=daysWrkVac, color='r', width=0.5)

plt.title('Total Days by Reporting Type', fontsize=14)
plt.margins(.12, .12)
plt.xticks(x, dates, fontsize=8.5, rotation=25, ha='right')
plt.ylabel('Amount of Reported Days')
plt.legend(loc=4)
plt.show()

# end
print('\nWork Plot No.4.. Total Days by Reporting Type.. Done!')
