from report import Report
from datetime import datetime as dt

# ----------------------
# Author: Haya Kornblau
# Date:  14/05/20 22:00
# ----------------------
from consts import dateTimeFormat

repType = 1  # Workday
repMode = ''


def report():
    # get empId
    empId = input('Please enter your Employee Id: ')
    udate = dt.now().strftime(dateTimeFormat)

    # get reporting mode
    entryExit = int(input('Please enter Entry/Exit type (1-Entry, 2-Exit): '))
    entryFlag = (entryExit == 1)

    if entryFlag:
        repMode = 'Insert'
        fromTime = udate
        tillTime = None

        print(fromTime)
        print(tillTime)

    else:
        repMode = 'UpdateExit'
        fromTime = None
        tillTime = udate

        print(fromTime)
        print(tillTime)

    # save to file
    print('Reporting WH for employee {}, report type {}, {} mode..'.format(empId, repType, repMode))

    # save - step 1 - create instance of report
    report_1 = Report(empId, repType, fromTime, tillTime)

    # save - step 2 - call by reporting mode
    if repMode == 'Insert':
        report_1.ins_report()
    elif repMode == 'UpdateExit':
        report_1.upd_report_exit()


# main
print('Reporting Working WH of an employee..\n')
report()
print('Done! Reporting Working WH of an employee\n')
