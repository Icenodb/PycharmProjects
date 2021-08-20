import tkinter as tk
import baseContr as bc


def openWindow():
    mainWin = bc.newWindow('学生管理')

    # 标题
    rowTitle = tk.Frame(mainWin)
    bc.newLabel(rowTitle, '学生管理', 13)
    rowTitle.pack()
    bc.newHr(mainWin)

    bc.newEmptyRow(mainWin)  # 显示分割线

    # 创建第一行对象
    row1 = tk.Frame(mainWin)
    # 学号
    sno = bc.newEntry(row1, '学号:  ')
    # 姓名
    sname = bc.newEntry(row1, '   姓名: ')
    row1.pack()

    bc.newEmptyRow(mainWin)  # 显示分割线

    row2 = tk.Frame(mainWin)  # 第二行控件
    # 性别
    sex = bc.newRadio(row2, [('男', '1'), ('女', '2'), ('不确定', 'x')], '性别', 'x')

    row2.pack()

    bc.newEmptyRow(mainWin)  # 显示分割线
    # 创建按钮对象
    rowButton = tk.Frame(mainWin)

    # 函数闭包--在一个函数里面,再定义一个函数
    def saveStudent():
        print(f"学号={sno.get()},姓名={sname.get()}")
        print(f"性别={sex.get()}")

    tk.Button(rowButton, text='  保存  ', command=saveStudent).pack(side='left')
    rowButton.pack()

    mainWin.mainloop()


if __name__ == "__main__":
    openWindow()
