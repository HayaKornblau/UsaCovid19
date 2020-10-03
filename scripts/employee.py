import pandas as pd
import datetime
from datetime import date, datetime
import logging

# -----------------------
# Author: Haya Kornblau
# Date  : 22/08/20 17:20
# -----------------------
# Source: employee.py
# Type  : Class
# -----------------------

class Employee:
    """Employee class"""
    logging.basicConfig(filename='../log/employeeLog.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    salary_raise_percent: float = 5.0
    salary_cut_percent: float = 3.0

    def __init__(self, empId, firstName, lastName, gender, birthDate, deptId, positionId, salary):
        self.empId = empId
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.birthDate = birthDate
        self.deptId = deptId
        self.positionId = positionId
        self.salary = salary

        logging.info('Created employee: {}-{}-{}'.format(self.empId, self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.firstName, self.lastName)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    @property
    def days_to_birthday(self):
        days_to_birthday: int = 0
        today = date.today()
        birth_date_obj: datetime = datetime.strptime(self.birthDate, '%Y-%m-%d')
        next_birthday = date(today.year, birth_date_obj.month, birth_date_obj.day)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        days_to_birthday = abs(next_birthday - today).days
        return days_to_birthday

    @property
    def happy_birthday(self):
        if self.days_to_birthday == 0:
            return 'Happy birthday!'
        return None

    def apply_salary_raise(self):
        self.salary = int(self.salary * (1 + self.salary_raise_percent / 100))
        logging.info('apply_salary_raise: empId {}, salary {}, '
                     'after raised by {}%'.format(self.empId, self.salary, self.salary_raise_percent))

    def apply_salary_cut(self):
        self.salary = int(self.salary / (1 + self.salary_cut_percent / 100))
        logging.info('apply_salary_cut: empId {}, salary {}, '
                     'after cut by {}%'.format(self.empId, self.salary, self.salary_cut_percent))

    def ins_employee(self):
        df_Emp = pd.read_csv('../data/tables/Employee.csv')
        new_row = {'empId': self.empId, 'firstName': self.firstName, 'lastName': self.lastName, 'gender': self.gender,
                   'birthDate': self.birthDate, 'deptId': self.deptId, 'positionId': self.positionId,
                   'salary': self.salary}
        print('employee >> ins_employee')
        print(new_row)
        df_Emp = df_Emp.append(new_row, ignore_index=True)
        print(df_Emp)
        df_Emp.to_csv('../data/tables/Employee.csv', index=False)
        logging.info('Inserted Employee: {}-{}-{}'.format(self.empId, self.fullname, self.email))

    def upd_employee(self):
        df_Emp = pd.read_csv('../data/tables/Employee.csv')
        df_Emp.loc[df_Emp['empId'] == self.empId, 'firstName'] = self.firstName
        df_Emp.loc[df_Emp['empId'] == self.empId, 'lastName'] = self.lastName
        df_Emp.loc[df_Emp['empId'] == self.empId, 'gender'] = self.gender
        df_Emp.loc[df_Emp['empId'] == self.empId, 'birthDate'] = self.birthDate
        df_Emp.loc[df_Emp['empId'] == self.empId, 'deptId'] = self.deptId
        df_Emp.loc[df_Emp['empId'] == self.empId, 'positionId'] = self.positionId
        df_Emp.loc[df_Emp['empId'] == self.empId, 'salary'] = self.salary
        print(df_Emp)
        df_Emp.to_csv('../data/tables/Employee.csv', index=False)
        logging.info('Updated Employee: {}-{}-{}'.format(self.empId, self.fullname, self.email))

    def del_employee(self):
        df_Emp = pd.read_csv('../data/tables/Employee.csv')
        df_Emp = df_Emp[df_Emp.empId != self.empId]
        print(df_Emp)
        df_Emp.to_csv('../data/tables/Employee.csv', index=False)
        logging.info('Deleted Employee: {}-{}-{}'.format(self.empId, self.fullname, self.email))

