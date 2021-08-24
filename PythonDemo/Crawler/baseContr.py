import sqlite3
import tkinter as tk
from tkinter import ttk

dbname = "douban.db"


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


def newSelect(root, labels: tuple, title: str = '', defVal: int = 0):
    """
    创建静态下拉列表
    :param root: 依附的容器
    :param labels: 下拉列表的元素
    :param title: 下拉列表的名字
    :param defVal: 默认值
    :return: 下拉列表对象
    """
    tk.Label(root, text=title).pack(side='left')
    com = ttk.Combobox(root, state='readonly')
    com.pack(side='left')
    com['values'] = labels
    com.current(defVal)
    return com


def newSelectReadFile(root, fileName: str, title: str = '', defVal: int = 0):
    """
    读取文件生成下拉列表
    :param root: 依附的容器
    :param fileName: 文件的名称
    :param title: 下拉列表的标题
    :param defVal: 默认被选中的项目的索引
    :return: 下拉列表对象，下拉列表对象的编码元组
    """
    tk.Label(root, text=title).pack(side='left')
    labels = []
    codes = []
    with open(fileName, 'r', encoding='utf-8') as fr:
        for row in fr:
            option = row.split(':')
            codes.append(option[0])
            labels.append(option[1])
    com = ttk.Combobox(root, state='readonly')
    com.pack(side=tk.LEFT)
    com['values'] = labels
    com.current(defVal)
    return com, codes


def getSelect(root, fname: str, title: str = '', defVal: int = 0):
    """
    读取数据库 生成下拉列表和下拉列表对象编码的元组
    :param root:依附的容器
    :param fname:要查询的列表名
    :param title:标题
    :param defVal:默认选中的值
    :return:下拉列表对象,下拉列表对象编码的元组
    """
    tk.Label(root, text=title).pack(side='left')
    # 为select控件定义code和label列表
    labels = []
    codes = []
    # 定义SQL语句
    sql = "select fcode,fvalue from syscode where isv=? and fname=?"
    # 连接数据库
    with sqlite3.connect(dbname) as conn:
        # 获取游标
        cursor = conn.cursor()
        # 基于游标执行SQL语句
        cursor.execute(sql, ['1', fname])
        # 读取查询结果
        rows = cursor.fetchall()
    # 解析查询结果,填充select的code和label列表
    for ins in rows:
        codes.append(ins[0])
        labels.append(ins[1])
    # 创建下拉列表控件
    com = ttk.Combobox(root, state='readonly')
    com.pack(side=tk.LEFT)
    # 挂接label
    com['values'] = labels
    # 指定默认值
    com.current(defVal)
    # 处理返回值
    return com, codes


def newText(root: tk.Frame, title: str, w: int = 45, h: int = 7):
    """
    创建带有滚动条的大文本域
    :param root:依附的容器
    :param title:标题
    :param w:宽
    :param h:高
    :return:文本域对象
    """
    tk.Label(root, text=title).pack(side='left')
    """大文本域"""
    # 创建文本框容器对象
    rowtext = tk.Frame(root)
    # 创建文本框text，设置宽度w，文本显示的行数设置为h行
    text = tk.Text(rowtext, width=w, font=('微软雅黑', 11), height=h)
    text.grid(row=4, column=1, sticky=tk.S + tk.W + tk.E + tk.N)
    # 创建滚动条
    scroll = tk.Scrollbar(rowtext, orient="vertical", command=text.yview)
    # 将滚动条填充
    text.config(yscrollcommand=scroll.set)
    # 将滚动条与文本框关联
    scroll['command'] = text.yview
    scroll.grid(row=4, column=2, sticky=tk.S + tk.W + tk.E + tk.N)
    rowtext.pack(side='left')
    return text


def newCheckBox(root, fname: str, title: str = '', ):
    """
    读取数据库 生成CheckBox
    :param root:依附的容器
    :param fname:要查询的列表名
    :param title:标题
    :param defVal:默认选中的值
    :return:CheckBox对象,CheckBox对象编码的元组
    """
    # 定义SQL语句
    sql = "select fcode,fvalue from syscode where isv=? and fname=?"
    # 连接数据库
    with sqlite3.connect(dbname) as conn:
        # 获取游标
        cursor = conn.cursor()
        # 基于游标执行SQL语句
        cursor.execute(sql, ['1', fname])
        # 读取查询结果
        rows = cursor.fetchall()
    # 解析查询结果,填充select的code和label列表
    tk.Label(root, text=title).pack(side='left')
    cbValues = []
    for ins in rows:
        var = tk.StringVar()
        CheckValue = ins[0]
        # print(CheckValue)
        CheckName = ins[1]
        # print(CheckName)
        tk.Checkbutton(root, text=CheckName, variable=var, onvalue=CheckValue, offvalue="").pack(side='left')
        cbValues.append(var)
    return cbValues


def printV(vs: list):
    print(vs)
    print(var.get() for var in vs if var)


def showDataTree(tree, rows):
    # ---删除原数据
    items = tree.get_children()  # 获取tree对象的数据集合
    [tree.delete(item) for item in items]
    # 显示查询结果
    colIndex = 0
    for row in rows:
        rowList = list(row)[1:]  # 将元组转换为list,并踢掉第一列的did
        rowList.insert(0, colIndex + 1)  # 为当前行数据增加序号
        # row_tup=tuple(rowList)
        # 给当前行添加一个无标题列,tree内部将该列标记为text,值为该条数据的主键
        tree.insert("", colIndex, text=row[0], values=rowList)
        colIndex = colIndex + 1


def reloadTreeView(tree):
    """重新加载TreeView的数据"""
    # 重新整理TreeView的数据,对数据重新编号,避免跳行
    # 获取TreeView的数据集对象
    items = list(tree.get_children())
    if items:
        print(f"items={items},focus={tree.focus()}")
        # 5.2.从items中,删除选中行的treeView标识
        items.remove(tree.focus())
        # 5.3.定义列表对象,装载整理后的原始数据
        rows = []
        # 5.4.遍历items中的每个treeView标识
        for item_id in items:
            # 5.5.获取该标识对应的行对象
            rowItem = tree.item(item_id)
            # 5.6.获取当前行的数据列表
            rowList = rowItem['values']
            # 5.7.将当前行数据列表的序号,替换为主键
            rowList[0] = rowItem['text']
            # 5.8.将当前行数据,放入rows
            rows.append(rowList)

        # 是否存在可以显示的数据
        if rows:
            # 显示数据
            showDataTree(tree, rows)


def newTree(root, titleTuple):
    """创建数据窗口对象"""
    cols = [title[0] for title in titleTuple]  # 创建表格的标题列表
    ybar = tk.Scrollbar(root, orient='vertical')  # 竖直滚动条
    tree = tk.ttk.Treeview(root,
                           show='headings',  # 隐藏text空列
                           height=16,
                           columns=cols,
                           yscrollcommand=ybar.set)

    # 表头设置--无需变更
    for col in cols:
        tree.heading(col, text=col, command=lambda col=col: tk.tree_sort_column(tree, col, False))  # 行标题
    # 设置各列的宽度--根据需要调整
    for title in titleTuple:
        tree.column(title[0], width=title[1], anchor=title[2])

    ybar['command'] = tree.yview
    tree.grid(row=0, column=0)  # grid方案
    ybar.grid(row=0, column=1, sticky='ns')
    return tree


if __name__ == "__main__":
    mainwin = newWindow('员工管理', 7)
    Values = newCheckBox(mainwin, "hobby", "爱好")
    # 显示窗口
    mainwin.mainloop()
