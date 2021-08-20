import tkinter as tk
from tkinter import ttk
import baseContr as bc

win = bc.newWindow()

comValue = ('java', 'C', 'C++', 'Python')

# 创建下拉列表控件
lan = ttk.Combobox(win, state='readonly')
lan.pack()
lan['values'] = comValue  # 下拉列表的数据
lan.current(1)  # 默认第几项被选中


def readCom():
    # 选中项目的数据,选中项目的索引
    print(lan.get(), lan.current())


tk.Button(win, text='测试', command=readCom).pack()

win.mainloop()
