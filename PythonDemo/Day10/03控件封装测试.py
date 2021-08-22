import tkinter as tk
import baseContr as bc
import sqlite3 as s3

# def openWindow():
#     mainWin = bc.newWindow('学生管理')
#
#     # 标题
#     rowTitle = tk.Frame(mainWin)
#     bc.newLabel(rowTitle, '学生管理', 13)
#     rowTitle.pack()
#     bc.newHr(mainWin)
#
#     bc.newEmptyRow(mainWin)  # 显示分割线
#
#     # 创建第一行对象
#     row1 = tk.Frame(mainWin)
#     # 学号
#     sno = bc.newEntry(row1, '学号:  ')
#     # 姓名
#     sname = bc.newEntry(row1, '   姓名: ')
#     row1.pack()
#
#     bc.newEmptyRow(mainWin)  # 显示分割线
#
#     row2 = tk.Frame(mainWin)  # 第二行控件
#     # 性别
#     sex = bc.newRadio(row2, [('男', '1'), ('女', '2'), ('不确定', 'x')], '性别', 'x')
#
#     row2.pack()
#
#     bc.newEmptyRow(mainWin)  # 显示分割线
#     # 创建按钮对象
#     rowButton = tk.Frame(mainWin)
#
#     # 函数闭包--在一个函数里面,再定义一个函数
#     def saveStudent():
#         print(f"学号={sno.get()},姓名={sname.get()}")
#         print(f"性别={sex.get()}")
#
#     tk.Button(rowButton, text='  保存  ', command=saveStudent).pack(side='left')
#     rowButton.pack()
#
#     mainWin.mainloop()
#
#
# if __name__ == "__main__":
#     openWindow()

"""
0.checkbox
1.将页面美化一下  
2. 创建一个学生表,将数据录入表中
提交方式,按照小组提交压缩包,每个人以姓名命名一个word文件,里面是项目运行截图和原代码截图


"""
dbname = "../Day08/az.db"


def openWindow():
    mainWin = bc.newWindow('学生管理')

    # 标题
    rowTitle = tk.Frame(mainWin)
    bc.newLabel(rowTitle, '学生管理', 13)
    rowTitle.pack()
    bc.newHr(mainWin)

    bc.newEmptyRow(mainWin)  # ---------显示分割线------------

    # 创建第一行对象
    row1 = tk.Frame(mainWin)
    # 学号
    sno = bc.newEntry(row1,'学号:')
    # 姓名
    sname = bc.newEntry(row1,'             姓名:     ')
    row1.pack()

    bc.newEmptyRow(mainWin)  # 显示分割线

    row2 = tk.Frame(mainWin)  # 第二行控件
    # 性别
    sex = bc.newRadio(row2, [('男', '1'), ('女', '2'), ('不确定', 'x')], '性别:', 'x')
    # 读取文件创建民族
    bc.newLabel(row2,"         ")
    nation, nationCodes = bc.getSelect(row2, 'nation', '民族:')

    row2.pack()

    bc.newEmptyRow(mainWin)  # ---------显示分割线------------

    row3 = tk.Frame(mainWin)
    # 学历
    edu, eduCodes = bc.getSelect(row3, 'education', '学历:')
    bc.newLabel(row3,"     ")
    # 所学专业--静态列表的玩法
    majorLabels = ('软件工程', '计算机科学与技术', '云计算', '物联网', '大数据', '人工智能')
    majorCodes = ('01', '02', '03', '04', '05', '06')
    major = bc.newSelect(row3, majorLabels, '专业:')
    row3.pack()
    bc.newEmptyRow(mainWin)  # ---------显示分割线------------
    row4 = tk.Frame(mainWin)
    values=bc.newCheckBox(row4, "hobby", "爱好:")
    row4.pack()
    bc.newEmptyRow(mainWin)  # ---------显示分割线------------

    row4 = tk.Frame(mainWin)
    smemo = bc.newText(row4, '备注')
    row4.pack()

    bc.newEmptyRow(mainWin)  # 显示分割线
    # 创建按钮对象
    rowButton = tk.Frame(mainWin)


    # 函数闭包--在一个函数里面,再定义一个函数
    def saveStudent():
        args=[]
        args.append(sno.get())
        args.append(sname.get())
        args.append(sex.get())
        args.append(majorCodes[major.current()])
        args.append(nationCodes[nation.current()])
        args.append(eduCodes[edu.current()])
        print(f"学号={sno.get()},姓名={sname.get()}")
        print(f"性别={sex.get()}")
        print(f"所学专业={major.get()},专业编码={majorCodes[major.current()]}")
        print(f"民族={nation.get()},该民族的编码是={nationCodes[nation.current()]}")
        print(f"学历={edu.get()},学历编码={eduCodes[edu.current()]}")
        hobbyvalue=",".join(var.get() for var in values if var.get()!="")
        args.append(hobbyvalue)
        args.append(smemo.get('0.0', 'end'))
        addStudent(args)
    tk.Button(rowButton, text='  保存  ', command=saveStudent).pack(side='left')
    rowButton.pack()

    def addStudent(args:list):
        sql = """insert into student("sno", "sname", "ssex", "smajor", "sedu", "snation", "shobby","smemo") 
        VALUES (?, ?,?, ?, ?, ?, ?,?);
        """
        with s3.connect(dbname) as conn:
            conn.execute(sql, args)
    mainWin.mainloop()


if __name__ == '__main__':
    openWindow()
