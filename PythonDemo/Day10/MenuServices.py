import tkinter as tk
import EmpWindow as ew


def initMenu(mainWin: tk.Tk):
    """菜单的全部处理"""
    # 创建主菜单
    mainMenu = tk.Menu()

    # 创建子菜单项
    deptMenu = tk.Menu(tearoff=0)
    deptMenu.add_command(label='部门创建')
    deptMenu.add_command(label='部门查询')
    deptMenu.add_command(label='部门维护')
    deptMenu.add_separator()  # 一条分割线
    deptMenu.add_command(label='部门分立')
    deptMenu.add_command(label='部门合并')
    deptMenu.add_command(label='部门裁汰')
    mainMenu.add_cascade(label='部门管理', menu=deptMenu)  # 将子菜单级联到主菜单上

    # 创建员工模块的菜单
    empMenu = tk.Menu(tearoff=0)

    def openEmp():
        mainWin.destroy()  # 销毁主窗口
        ew.openWindow()  # 打开员工管理窗口

    empMenu.add_command(label='员工建档', command=openEmp)
    empMenu.add_command(label='员工离职')
    empMenu.add_command(label='员工退休')
    empMenu.add_command(label='员工死亡')
    empMenu.add_command(label='部门调转')
    empMenu.add_command(label='员工调薪')
    mainMenu.add_cascade(label='员工管理', menu=empMenu)  # 挂接到主菜单

    # 系统维护
    sysMenu = tk.Menu(tearoff=0)
    sysMenu.add_command(label='口令维护')
    sysMenu.add_separator()  # 一条分割线

    def exitMainWindow():
        # 销毁主窗口
        mainWin.destroy()

    sysMenu.add_command(label='退出', command=exitMainWindow)
    mainMenu.add_cascade(label='系统维护', menu=sysMenu)

    # 将菜单挂接到窗口上
    mainWin.config(menu=mainMenu)
