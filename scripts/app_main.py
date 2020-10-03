import os
from tkinter import *
from PIL import Image, ImageTk

# ----------------------
# Author: Haya Kornblau
# Date  : 03/10/20 13:30
# ----------------------
# Source: app_main.py
# ----------------------


def appEmployeeCmd():
    os.system('python app_employee.py')


def EmpDetailsCmd():
    os.system('python emp_details.py')


def EmpAttendanceDetailsCmd():
    os.system('python attendance_details.py')


def deptDetailsCmd():
    os.system('python dept_details.py')


def positionDetailsCmd():
    os.system('python position_details.py')


def managerDetailsCmd():
    os.system('python manager_details.py')


# app attendance
def appAttendanceWrkCmd():
    os.system('python app_attendance_wrk.py')


def appAttendanceVacCmd():
    os.system('python app_attendance_vac.py')


def appAttendanceSckCmd():
    os.system('python app_attendance_sck.py')


# app board
def appBoardEmpCmd():
    os.system('python app_board_by_emp.py')


def appBoardEmpSalaryCmd():
    os.system('python app_board_emp_by_salary.py')


def appBoardSalaryDeptCmd():
    os.system('python app_board_salary_by_dept.py')


def appBoardMngrEmpDeptCmd():
    os.system('python app_board_dept_mngr_emp.py')


def appBoardAttendanceCmd():
    os.system('python app_board_attendance_by_date.py')


# app plot
def deptPlot1Cmd():
    os.system('python plot_d1_wrk_by_dept.py')


def deptPlot2Cmd():
    os.system('python plot_d2_sal_percent_by_dept.py')


def deptPlot3Cmd():
    os.system('python plot_d3_sal_statistics_by_dept.py')


def attendancePlot1Cmd():
    os.system('python plot_r1_wrk_per_date.py')


def attendancePlot2Cmd():
    os.system('python plot_r2_vac_per_date.py')


def attendancePlot3Cmd():
    os.system('python plot_r3_sck_per_date.py')


def attendancePlot4Cmd():
    os.system('python plot_r4_stacked_days_by_rep_type.py')


def openHelpWindow():
    helpWindow = Toplevel()
    helpWindow.title('Help')
    helpWindow.geometry("373x152")
    Label(helpWindow, text="\n\n     Help Us Save the World from Covid-19 !!!     \n\n\n\n\n",
          font='Verdana 11 italic',
          foreground='white', background='navy').pack()


def openAboutWindow():
    aboutWindow = Toplevel()
    aboutWindow.title('About')
    aboutWindow.geometry("405x164")
    aboutWindow.geometry("364x182")
    Label(aboutWindow, text="\n                    Implemented & Developed by                      ",
          font='Verdana 9',
          foreground='white', background='#3F4C6A').pack()
    Label(aboutWindow, text="\n                      Haya Kornblau                       ",
          font='Verdana 12 bold',
          foreground='white', background='#3F4C6A').pack()
    Label(aboutWindow, text='\n\n\n\n            Special Python-Corona TaskForce ' + chr(169) + ' 2020           \n\n',
          font='Verdana 9',
          foreground='white', background='#3F4C6A').pack()


# Covid-19
covid19App = Tk()  # menu instance
covid19App.title('Covid-19 TaskForce Attendance App')
menu = Menu(covid19App)
covid19App.config(menu=menu)
covid19App.geometry("840x450+10+20")
loadImgBg = Image.open('../images/img_main_covid.jpg')
renderImgBg = ImageTk.PhotoImage(loadImgBg)
imgBg = Label(covid19App, image=renderImgBg)
imgBg.image = renderImgBg
imgBg.place(x=0, y=0)

# Main menu
mainMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Task Force', menu=mainMenu)

# Emp menu
empMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='Employee', menu=empMenu)
mainMenu.add_separator()
empMenu.add_command(label='Employee Form', command=appEmployeeCmd)
empMenu.add_separator()
empMenu.add_command(label='Employee Details', command=EmpDetailsCmd)
empMenu.add_command(label='Attendance Details', command=EmpAttendanceDetailsCmd)

# Dept menu
deptMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='Dept', menu=deptMenu)
deptMenu.add_command(label='Dept Details', command=deptDetailsCmd)
deptPlotMenu = Menu(menu, tearoff=0)
deptMenu.add_cascade(label='Dept Plot', menu=deptPlotMenu)
deptPlotMenu.add_command(label='Plot Work Days by Dept', command=deptPlot1Cmd)
deptPlotMenu.add_command(label='Plot Salary Percent by Dept', command=deptPlot2Cmd)
deptPlotMenu.add_command(label='Plot Salary Statistics by Dept', command=deptPlot3Cmd)

# Position menu
PositionMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='Position', menu=PositionMenu)
PositionMenu.add_command(label='Position Details', command=positionDetailsCmd)

# Manager menu
managerMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='Manager', menu=managerMenu)
managerMenu.add_command(label='Manager Details', command=managerDetailsCmd)

# Exit
mainMenu.add_separator()
mainMenu.add_command(label='Exit', command=covid19App.quit)

# Attendance menu
AttendanceMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Attendance', menu=AttendanceMenu)
AttendanceMenu.add_command(label='Report Work Hours', command=appAttendanceWrkCmd)
AttendanceMenu.add_command(label='Report Vacation', command=appAttendanceVacCmd)
AttendanceMenu.add_command(label='Report Sickness', command=appAttendanceSckCmd)

# Report Boards menu
reportBoardMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Reports', menu=reportBoardMenu)
reportBoardMenu.add_command(label='Employee Report', command=appBoardEmpCmd)
reportBoardMenu.add_command(label='Attendance Report', command=appBoardAttendanceCmd)
reportBoardMenu.add_separator()
reportBoardMenu.add_command(label='Employee by Salary', command=appBoardEmpSalaryCmd)
reportBoardMenu.add_command(label='Salaries by Dept', command=appBoardSalaryDeptCmd)
reportBoardMenu.add_command(label='Managers & Emps by Depts', command=appBoardMngrEmpDeptCmd)

# Plot menu
plotMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Plots', menu=plotMenu)

deptPlotMenu = Menu(menu, tearoff=0)
plotMenu.add_cascade(label='Dept Plot', menu=deptPlotMenu)
deptPlotMenu.add_command(label='Plot Work Days by Dept', command=deptPlot1Cmd)
deptPlotMenu.add_command(label='Plot Salary Percent by Dept', command=deptPlot2Cmd)
deptPlotMenu.add_command(label='Plot Salary Statistics by Dept', command=deptPlot3Cmd)
plotMenu.add_separator()

attendancePlotMenu = Menu(menu, tearoff=0)
plotMenu.add_cascade(label='Attendance Plot', menu=attendancePlotMenu)
attendancePlotMenu.add_command(label='Plot Work Days per Date', command=attendancePlot1Cmd)
attendancePlotMenu.add_command(label='Plot Vacation Days per Date', command=attendancePlot2Cmd)
attendancePlotMenu.add_command(label='Plot Sickness Days per Date', command=attendancePlot3Cmd)
attendancePlotMenu.add_separator()
attendancePlotMenu.add_command(label='Plot Days by Attendance Type', command=attendancePlot4Cmd)

# Help menu
HelpMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=HelpMenu)
HelpMenu.add_command(label='Help', command=openHelpWindow)
HelpMenu.add_command(label='About', command=openAboutWindow)

# main
mainloop()
