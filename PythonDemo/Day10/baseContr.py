import tkinter as tk


def newWindow(title: str = '新窗口', up: int = 5, width: int = 160, height: int = 90,
              offset: int = 40, resize: bool = False):
    """
    :param title: 窗体标题
    :param up: 放大倍数
    :param width: 宽度
    :param height: 高度
    :param offset: 起始位置的偏移量
    :param resize: 是否允许放大
    :return: 窗体对象
    """
    win = tk.Tk()
    win.title(title)
    w = width * up
    h = height * up
    # 获取屏幕的高度和宽度
    scw = win.winfo_screenwidth()
    sch = win.winfo_screenheight()
    # 设置窗口的起始坐标
    x = (scw - w) / 2 - offset
    y = (sch - h) / 2 - offset
    # 重构窗口的几何属性，让以上属性设置生效
    win.geometry("%dx%d+%d+%d" % (w, h, x, y))
    win.resizable(resize, resize)
    return win
