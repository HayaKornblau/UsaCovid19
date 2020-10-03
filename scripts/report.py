import logging
import pandas as pd


# ----------------------
# Author: Haya Kornblau
# Date  : 14/05/20 22:10
# ----------------------


class Report:
    """Report class"""
    logging.basicConfig(filename='../log/reportLog.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    def __init__(self, empId, repType, fromTime, tillTime):
        self.empId = empId
        self.repType = repType  # (1-Workday, 2-Vacation, 3-Sick)
        self.fromTime = fromTime
        self.tillTime = tillTime

        logging.info('Reporting of employee: {}, {}, {}, {} init'.
                     format(self.empId, self.repType, self.fromTime, self.tillTime))

    def ins_report(self):
        df_Report = pd.read_csv('../data/tables/Report.csv')
        new_row = {'empId': self.empId, 'repType': self.repType, 'fromTime': self.fromTime, 'tillTime': self.tillTime}
        print(new_row)
        df_Report = df_Report.append(new_row, ignore_index=True)
        print(df_Report)
        df_Report.to_csv('../data/tables/Report.csv', index=False)
        print('End insReport')

    def upd_report_exit(self):
        df_Report = pd.read_csv('../data/tables/Report.csv')
        print(df_Report.loc[(df_Report['empId'] == int(self.empId)) & (df_Report['repType'] == int(self.repType)),
                            ['tillTime']])
        df_Report.loc[(df_Report['empId'] == int(self.empId)) & (df_Report['repType'] == int(self.repType))
                      & (df_Report['tillTime'].isna()), ['tillTime']] = self.tillTime

        df_Report.to_csv('../data/tables/Report.csv', index=False)
        print('End updReportExit')
