import baseContr as bc
import MainWindow as mw
import tkinter as tk


def openWindow():
    win = bc.newWindow("员工管理")

    initContr(win)

    def closeThis():
        # #销毁当前窗口
        win.destroy()
        # #打开主窗口
        mw.openWindow()

    # 添加事件拦截方法
    win.protocol("WM_DELETE_WINDOW", closeThis)

    win.mainloop()


def initContr(win: tk.Tk):
    """完成控件挂接"""
    print("为当前窗口挂接控件.....")
