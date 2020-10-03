from consts import *
from report import Report
from datetime import datetime as dt

# ----------------------
# Author: Haya Kornblau
# Date:  14/05/20 22:10
# ----------------------

repType = 3  # Sickness
repMode = 'Insert'


def report():
    # get empId
    empId = input('Please enter your Employee Id: ')

    # get fromDate ..
    while True:
        try:
            fTime = input('Please enter Entry Time in [YYYY-MM-DD hh:mm] format: ')  # 2020-12-05 08:24
            fromTime = dt.strptime(fTime, dateTimeFormat)
        except ValueError:
            print('Oops! Invalid date..')
            # try again.. go to start of the loop
            continue
        else:
            # fromTime was successfully parsed!
            # exit the loop.
            break

    # get tillDate..
    while True:
        try:
            tTime = input('Please enter Exit Time in [YYYY-MM-DD hh:mm] format: ')  # 2020-12-05 08:24
            tillTime = dt.strptime(tTime, dateTimeFormat)
        except ValueError:
            print('Oops! Invalid date..')
            # try again.. goto start of the loop
            continue
        else:
            print('timediff')
            print(fromTime)
            print(tillTime)
            tdiff = tillTime - fromTime
            print(tdiff.days)
            print(tdiff.seconds)
            cDaysDiff = tillTime.day - fromTime.day  # calendar days diff
            print(cDaysDiff)
            if cDaysDiff != 0:
                print('Oops! Invalid Exit day.. Exit day must be the same as Entry day..')
            elif tdiff.seconds < 0:
                print('Oops! Invalid Exit time.. Exit time must be after Entry time..')
            elif tdiff.seconds > SEC_IN_WRK_DAY:
                print('Oops! You are allowed to report up to {} hours per day..'.format(HRS_IN_WRK_DAY))
            else:
                # tillTime was successfully parsed!
                # exit the loop.
                break

    print(fromTime)
    print(tillTime)

    # save to file
    print('Reporting WH for employee {}, report type {}, {} mode..'.format(empId, repType, repMode))
    report_1 = Report(empId, repType, fromTime, tillTime)
    report_1.ins_report()


# main
print('Reporting Sickness WH of an employee..\n')
report()
print('Done! Reporting Sickness WH of an employee\n')
