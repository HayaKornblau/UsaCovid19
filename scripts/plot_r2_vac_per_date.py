import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------
# Author: Haya Kornblau
# Date  : 15/05/20 14:55
# --------------------------------------------
# Source: WorkPlot#2 - Vacation Days per Date
# --------------------------------------------

# init
print('\nWork Plot No.2.. Vacation Days per Date.. Start')

# fetch data
print('\nWork Plot No.2.. Vacation Days per Date.. fetch TotReportByDateType..\n')
df_TotDaysByDate = pd.read_csv('../data/temp/TotReportByDateType.csv')
print(df_TotDaysByDate)

# plot
print('\nWork Plot No.2.. Vacation Days per Date.. plotting..')
dates = df_TotDaysByDate.date
x = np.arange(len(dates))
y = df_TotDaysByDate.vacDays
plt.xticks(x, dates, fontsize=8.5, rotation=25, ha='right')
plt.ylabel('Amount of Vacation Days')
plt.title('Total Vacations per Date', fontsize=14)
plt.bar(dates, y, color='y')
plt.show()

# end
print('\nWork Plot No.2.. Vacation Days per Date.. Done!\n')
