import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------
# Author: Haya Kornblau
# Date:  08/08/20 17:25
# --------------------------------------------
# Source: WorkPlot#3 - Sickness Days per Date
# --------------------------------------------

# init
print('\nWork Plot No.3.. Sickness Days per Date.. Start')

# fetch data
print('\nWork Plot No.3.. Sickness Days per Date.. fetch TotReportByDateType..\n')
df_TotDaysByDate = pd.read_csv('../data/temp/TotReportByDateType.csv')
print(df_TotDaysByDate)

# plot
print('\nWork Plot No.3.. Sickness Days per Date.. plotting..')
dates = df_TotDaysByDate.date
x = np.arange(len(dates))
y = df_TotDaysByDate.sckDays
plt.xticks(x, dates, fontsize=8.5, rotation=25, ha='right')
plt.ylabel('Amount of Sick Days')
plt.title('Total Sick Days per Date', fontsize=14)
plt.bar(dates, y, color='r')
plt.show()

# end
print('\nWork Plot No.3.. Sickness Days per Date.. Done!\n')
