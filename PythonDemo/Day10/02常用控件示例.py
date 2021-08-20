import tkinter as tk
import baseContr as bc

"""
1创建窗体
2创建容器Frame
3在容器里创建Lable,即显示的标签文字
4在容器里创建Entry,输入文本框
5显示容器pack()
"""

# 创建窗口对象
mainWin = bc.newWindow()
# 绘制一条线 fill='x'表示灌满横坐标 bg='#fff'
tk.Frame(mainWin, height=8).pack(fill='x')
# 创建容器
row1 = tk.Frame(mainWin)
# 学号
tk.Label(row1, text='学号:  ').pack(side='left')
# 文本框
sno = tk.StringVar()
tk.Entry(row1, textvariable=sno).pack(side='left')
# 空格
tk.Label(row1, text='    ').pack(side='left')
# 姓名
tk.Label(row1, text='姓名:  ').pack(side='left')
sname = tk.StringVar()
tk.Entry(row1, textvariable=sname).pack(side='left')

# 显示容器
row1.pack()
# 创建第二行的对象
row2 = tk.Frame(mainWin)


def saveStudent():
    vsname = sname.get()
    vsno = sno.get()
    print(f"学号={vsno},姓名={vsname}")


tk.Button(row2, text='保存', command=saveStudent).pack(side='left')
row2.pack()
mainWin.mainloop()
