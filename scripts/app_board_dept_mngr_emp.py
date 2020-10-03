import pandas as pd

# ----------------------
# Author: Haya Kornblau
# Date: 18/05/20 16:40
# ----------------------

# init
print('\nBoard of Dept Managers & Emps.. Start')

print('\nBoard of Dept Managers & Emps.. fetching emp..1\n')
pd.set_option('mode.chained_assignment', None)
df_Emp = pd.read_csv('../data/tables/Employee.csv')
df_Emp = df_Emp[['empId', 'firstName', 'lastName', 'deptId']]
print(df_Emp)

print('\nBoard of Dept Managers & Emps.. fetching dept..2\n')
df_Dept = pd.read_csv('../data/tables/Dept.csv')
print(df_Dept)

print('\nBoard of Dept Managers & Emps.. merging dept..3\n')
df_EmpDet = pd.merge(df_Emp, df_Dept, on='deptId')
print(df_EmpDet)

print('\nBoard of Dept Managers & Emps.. prep merging manager..4\n')
df_Manager = pd.read_csv('../data/tables/Manager.csv')
df_DeptMngrEmp = pd.merge(df_EmpDet, df_Manager, how='left', on='empId')
df_DeptMngrEmp = df_DeptMngrEmp.dropna()
df_DeptMngrEmp['managerId'] = df_DeptMngrEmp['managerId'].astype(int)
print(df_DeptMngrEmp)

print('\nBoard of Dept Managers & Emps.. merging manager..5\n')
df_Emp = df_Emp[['empId', 'firstName', 'lastName']]
df_DeptMngrEmp = pd.merge(df_DeptMngrEmp, df_Emp, how='left',
                          left_on='managerId', right_on='empId', suffixes=('', '_Manager'))
df_DeptMngrEmp.rename(columns={'firstName_Manager': 'managerFirstName',
                               'lastName_Manager': 'managerLastName'}, inplace=True)
print(df_DeptMngrEmp)

print('\nBoard of Dept Managers & Emps.. filtering..6')
df_DeptMngrEmp = df_DeptMngrEmp.filter(['deptId', 'deptName', 'managerFirstName', 'managerLastName',
                                        'firstName', 'lastName'])
cols = list(df_DeptMngrEmp.columns)
print('\nList of columns..')
print(cols)
print('\n')
print(df_DeptMngrEmp)

# get manager
deptType = input('\nPlease enter dept input type, or leave empty for select all(1-Id, 2-Name): ')

if deptType == '1':
    deptId = int(input('Please enter Dept Id: '))
    df_query = df_DeptMngrEmp[df_DeptMngrEmp.deptId == deptId]

elif deptType == '2':
    deptName = input('Please enter Dept name: ')
    df_query = df_DeptMngrEmp[df_DeptMngrEmp.deptName == deptName]

else:
    df_query = df_DeptMngrEmp

# print results
print('\nBoard of Employee Salaries by Range.. Results\n')
print(df_query)

# save data to file
saveToFileInput = input('\nSave report (Y/N)? ')
saveFlag = saveToFileInput.upper() == 'Y'

if saveFlag:
    saveToFile = input("\nEnter file the name of your text file - please use / backslash when typing path: ")
    # C:/Users/User/PycharmProjects/UsaCovid19/docs/deptMngrEmp_150820_1628.csv

    print('\nBoard of Dept Managers & Emps.. save to file..')
    df_query.to_csv(saveToFile, index=False)

# end board
print('\nBoard of Dept Managers & Emps.. Done!\n')
