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


def newLabel(root, title, fontsize=12):
    """创建标签对象"""
    tk.Label(root, text=title, font=('微软雅黑', fontsize)).pack(side='left')


def newEntry(root, title):
    """
    创建带有标签的单行文本框对象
    :param root: 依附的容器
    :param title: 标题
    :return: value 返回的文本框值对象
    """
    tk.Label(root, text=title).pack(side='left')
    value = tk.StringVar()
    tk.Entry(root, textvariable=value).pack(side='left')
    return value


def newHr(root, color='#F0F0F0', w=160):
    """
    可以自定义长度的线段
    :param root: 依附的容器
    :param color: 颜色
    :param w: 长度
    :return: 无
    """
    tk.Frame(root, bg=color, width=w, height=2).pack()


def newEmptyRow(root):
    """
    显示空行,行的分割线
    :param root: 依附的容器
    """
    tk.Frame(root, height=10).pack()


def newRadio(root, data, title='', defVal='1'):
    """
    创建单选按钮
    :param root: 依附的容器
    :param data: 单选按钮元数据组
    :param title: 标题
    :param defVal: 默认选择某个单选按钮
    :return: 单选按钮值对象
    """
    tk.Label(root, text=title).pack(side='left')
    # 定义单选按钮的数据容器
    value = tk.StringVar()
    value.set(defVal)
    # 循环data对象，创建单选按钮组
    for tup in data:
        tk.Radiobutton(root, value=tup[1], text=tup[0], variable=value).pack(side='left')
    return value


if __name__ == "__main__":
    mainwin = newWindow('员工管理', 7)
    # 显示窗口
    mainwin.mainloop()
