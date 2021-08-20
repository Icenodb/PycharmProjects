# 导入GTK
import tkinter as tk

# 创建窗体对象
win = tk.Tk()
# 设置窗体标题
win.title("测试窗体")
# 放大的比例
up = 5
# 窗口的大小
win_width = 160 * up
win_height = 90 * up
# 获取屏幕的高度和宽度
scw = win.winfo_screenwidth()
sch = win.winfo_screenheight()
# 设定窗口的起始坐标
x = (scw - win_width) / 2 - 40
y = (sch - win_height) / 2 - 40
# 修改窗口的几何属性
win.geometry("%dx%d+%d+%d" % (win_width, win_height, x, y))
# 禁止窗口放大
win.resizable(False, False)
# 创建窗口 进入消息循环
win.mainloop()
