from consts import *
import pandas as pd

# ----------------------
# Author: Haya Kornblau
# Date  : 15/05/20 22:35
# ----------------------


def calcHours(datetime):
    return datetime.dt.hour * MINUTES_IN_HOUR + datetime.dt.minute


def calcHoursDiff(fromTime, tillTime):
    return (calcHours(tillTime) - calcHours(fromTime)) / MINUTES_IN_HOUR


print('\nWork Hours Details.. start')
try:
    print('\ntry-except block.. start')
    df_Report = pd.read_csv('bad_file_name.csv')
except FileNotFoundError as fileErr:
    print(fileErr)
finally:
    df_Report = pd.read_csv('../data/tables/Report.csv')
    print('\n')
    print(df_Report)
    print('\ntry-except block.. end')

print('\nWork Hours Details.. fetching emp..')
df_EmpDetails = pd.read_csv('../data/temp/EmpDetails.csv')
print(df_EmpDetails)

print('\nWork Hours Details.. fetching dept..')
df_Dept = pd.read_csv('../data/tables/dept.csv')
print(df_Dept)

print('\nWork Hours Details.. merging..')
df_ReportDetails = pd.merge(df_Report, df_EmpDetails, on='empId')
print(df_ReportDetails)

df_ReportDetails['fromTime'] = pd.to_datetime(df_ReportDetails.fromTime, format=dateTimeFormatSlash)
df_ReportDetails['tillTime'] = pd.to_datetime(df_ReportDetails.tillTime, format=dateTimeFormatSlash)
print(df_ReportDetails)

print('\nReport Work Hours Details.. formatting date..')
df_ReportDetails['date'] = df_ReportDetails.fromTime.dt.date
print(df_ReportDetails)

print('\nWork Hours Details.. calc hours..')
df_ReportDetails['hours'] = calcHoursDiff(df_ReportDetails['fromTime'], df_ReportDetails['tillTime'])

print('\nWork Hours Details. calc wrk/vac/sck hours..')
df_ReportDetails['wrkHours'] = df_ReportDetails.apply(lambda x: x['hours'] if x['repType'] == 1 else 0, axis=1)
df_ReportDetails['vacHours'] = df_ReportDetails.apply(lambda x: x['hours'] if x['repType'] == 2 else 0, axis=1)
df_ReportDetails['sckHours'] = df_ReportDetails.apply(lambda x: x['hours'] if x['repType'] == 3 else 0, axis=1)
print(df_ReportDetails)

print('\nWork Hours Details.. calc wrk/vac/sck days..')
df_ReportDetails['days'] = list(map(lambda x: x / HRS_IN_WRK_DAY, df_ReportDetails['hours']))
df_ReportDetails['wrkDays'] = list(map(lambda x: x / HRS_IN_WRK_DAY, df_ReportDetails['wrkHours']))
df_ReportDetails['vacDays'] = list(map(lambda x: x / HRS_IN_WRK_DAY, df_ReportDetails['vacHours']))
df_ReportDetails['sckDays'] = list(map(lambda x: x / HRS_IN_WRK_DAY, df_ReportDetails['sckHours']))
print(df_ReportDetails)

print('\nWork Hours Details.. calc wrkDays by depts..')
for deptName in df_Dept['deptName']:
    df_ReportDetails['wrkDays' + deptName] = \
        df_ReportDetails.apply(lambda x: x['wrkDays'] if x['deptName'] == deptName else 0, axis=1)

df_ReportDetails.to_csv('../data/temp/ReportDetails.csv', index=False)
df_ReportDetails = pd.read_csv('../data/temp/ReportDetails.csv')
print(df_ReportDetails)

print('\nWork Hours Details.. group by date..')
df_TotReportByDateType = df_ReportDetails.groupby('date').sum()
df_TotReportByDateType = df_TotReportByDateType.drop(['empId', 'repType', 'salary'], axis=1)
df_TotReportByDateType.to_csv('../data/temp/TotReportByDateType.csv')
print(df_TotReportByDateType)

print('\nWork Hours Details.. Done!')
