from consts import *
from employee import Employee
from datetime import datetime as dt


# ------------------------
# Author: Haya Kornblau
# Date  : 22/08/20 18:30
# ------------------------
# Source: app_employee.py
# ------------------------


def updEmpDetails():
    # init
    okFlag = True

    # init emp
    empId: int = 0
    firstName = ''
    lastName = ''
    gender = '\0'
    birthDate = '1900-01-01'
    deptId = 0
    positionId = 0
    salary = 0

    # get update mode
    updMode = int(input('Please enter Update Mode (1-Insert, 2-Update, 3-Delete): '))

    # update by mode type
    if updMode in (1, 2):  # [1- Insert, 2-Update]
        empId = int(input('Please enter Employee Id: '))
        firstName = input('Please enter Employee First Name: ')
        lastName = input('Please enter Employee Last Name: ')
        gender = input('Please enter Gender (M/F): ')
        birthDateTmp = input('Please enter Birthdate in [YYYY-MM-DD] format: ')  # 1968-12-05
        birthDate = dt.strptime(birthDateTmp, dateFormat)
        deptId = int(input('Please enter Department Id: '))
        positionId = int(input('Please enter Position Id: '))
        salary = int(input('Please enter Employee Salary: '))

    elif updMode == 3:  # [3- Delete]
        empId = int(input('Please enter Employee Id: '))

    else:
        okFlag = False
        print('Oops! Updating Mode is not valid.')

    # save to file
    if okFlag:
        print('\nEmployee Details:')
        print(' Emp Id =', empId)
        print(' First Name =', firstName)
        print(' Last Name =', lastName)
        print(' Update Mode =', updMode, '\n')

        # step 1 -  create instance of employee
        emp1 = Employee(empId, firstName, lastName, gender, birthDate, deptId, positionId, salary)

        # step 2 -  activate emp method by updMode
        if updMode == 1:
            emp1.ins_employee()
        elif updMode == 2:
            emp1.upd_employee()
        elif updMode == 3:
            emp1.del_employee()


# main
print('\nUpdating of an employee..\n')
updEmpDetails()

print('\nUpdating of an employee.. Done!\n')
