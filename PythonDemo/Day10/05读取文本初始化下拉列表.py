import tkinter as tk
from tkinter import ttk
import baseContr as bc

win = bc.newWindow()
# 1.读取文本文件，生成下拉列表的文本和编码元组
# 定义下拉列表的标签与编码列表
lables = []
codes = []

with open('nation.txt', 'r', encoding='utf-8') as fr:
    for row in fr:
        option = row.split(':')
        codes.append(option[0])
        lables.append(option[1])

nation = ttk.Combobox(win, state='readonly')
nation.pack()
nation['values'] = lables
nation.current(0)


def add():
    print(f"民族={nation.get()},该民族编码={codes[nation.current()]}")


tk.Button(win, text='确定', command=add).pack()

win.mainloop()
