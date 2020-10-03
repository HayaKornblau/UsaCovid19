import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------
# Author: Haya Kornblau
# Date:  08/08/20 17:10
# ----------------------------------------
# Source: WorkPlot#1 - Work Days per Date
# ----------------------------------------

# init
print('\nWork Plot No.1.. Work Days per Date.. Start')

# fetch data
print('\nWork Plot No.1.. Work Days per Date.. fetch TotReportByDateType..\n')
df_TotDaysByDate = pd.read_csv('../data/temp/TotReportByDateType.csv')
print(df_TotDaysByDate)

# plot
print('\nWork Plot No.1.. Work Days per Date.. plotting..')
dates = df_TotDaysByDate.date
x = np.arange(len(dates))
y = df_TotDaysByDate.wrkDays
plt.xticks(x, dates, fontsize=8.5, rotation=25, ha='right')
plt.ylabel('Amount of Work Days')
plt.title('Work Days per Date', fontsize=14)
plt.bar(dates, y, color='b')
plt.show()

# end
print('\nWork Plot No.1.. Work Days per Date.. Done!\n')
