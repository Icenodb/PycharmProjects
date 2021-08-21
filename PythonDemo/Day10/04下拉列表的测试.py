import tkinter as tk
from tkinter import ttk
import baseContr as bc

win = bc.newWindow()

comValue = ('java', 'C', 'C++', 'Python')
comCode=('01','02','03','04')        #读取文本对应的code
# 创建下拉列表控件
lan = ttk.Combobox(win, state='readonly')
lan.pack()
lan['values'] = comValue  # 下拉列表的数据
lan.current(1)  # 默认第几项被选中


def readCom():
    # 选中项目的数据,选中项目的索引
    print(f"当前选中的是{lan.get()},其编码是{comCode[lan.current()]}")


tk.Button(win, text='测试', command=readCom).pack()

win.mainloop()
