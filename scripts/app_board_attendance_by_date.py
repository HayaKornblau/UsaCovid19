from consts import *
from datetime import datetime as dt
import pandas as pd

# ----------------------
# Author: Haya Kornblau
# Date: 18/05/20 23:20
# ---------------------

# init
print('Board by Reported Work Hours by Dates.. Start')

# fetch data
pd.set_option('mode.chained_assignment', None)
df_TotDaysByDate = pd.read_csv('../data/temp/TotReportByDateType.csv')
print('\nList of Reported Work Hours..\n')
print(df_TotDaysByDate)

# get dates
fTime = input('\nPlease enter From Date in [YYYY-MM-DD] format: ')  # 2020-12-05
fromTime = dt.strptime(fTime, dateFormat)

tTime = input('Please enter Till Date in [YYYY-MM-DD] format: ')  # 2020-12-08
tillTime = dt.strptime(tTime, dateFormat)

df_query = \
    df_TotDaysByDate[(df_TotDaysByDate['date'] >= fTime) &
                  (df_TotDaysByDate['date'] <= tTime)]

# get Hrs/Days Type
hrsDaysType = input('Please enter Hours/Days report type (1-Hours, 2-Days): ')
hrsDaysFlag = hrsDaysType == 1

if hrsDaysFlag:
    df_query = df_query[['date', 'hours', 'wrkHours', 'vacHours', 'sckHours']]
else:
    df_query = df_query[['date', 'days', 'wrkDays', 'vacDays', 'sckDays']]

# print results
print('\nBoard by Reported Work Hours by Dates.. Results\n')
print(df_query)

# save data to file
saveToFileInput = input('\nSave report (Y/N)? ')
saveFlag = saveToFileInput.upper() == 'Y'

if saveFlag:
    saveToFile = input("\nEnter file the name of your text file - please use / backslash when typing path: ")
    # C:/Users/User/source/repos/PyProjs/UsaCovid19/docs/WhReportByDate_150820_1628.csv

    # save report
    print('\nBoard by Reported Work Hours by Dates.. save to file..')
    df_query.to_csv(saveToFile, index=False)

# end board
print('\nBoard by Reported Work Hours by Dates.. Done!\n')
