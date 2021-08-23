import baseContr as bc
import tkinter as tk
import FilmServices as fs
from tkinter import ttk
import MainWindow as mw


def openWindow():
    win = bc.newWindow("影片管理----数据窗口封装测试", 6)
    initContr(win)
    # def closeThis():
    #     # #销毁当前窗口
    #     win.destroy()
    #     # #打开主窗口
    #     mw.openWindow()
    # #添加事件拦截方法
    # win.protocol("WM_DELETE_WINDOW",closeThis)
    win.mainloop()


def initContr(win: tk.Tk):
    """完成控件挂接"""
    bc.newEmptyRow(win)  # -------------分割线--------------
    # 创建标题行
    rowTitle = tk.Frame(win)
    bc.newLabel(rowTitle, "影片管理")
    rowTitle.pack()
    bc.newHr(win)

    bc.newEmptyRow(win)  # -------------分割线--------------
    # 添加数据窗口
    row1 = tk.Frame(win)
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    titleTuple = (('序号', 60, 'center'),
                  ('影片编号', 200, 'center'),
                  ('影片名称', 200, 'center'))
    tree = bc.newTree(row1, titleTuple)

    # 为treeview绑定双击事件
    def delrow(event):  # 双击事件的脚本程序
        curItem = tree.focus()  # 选中行在tree中的id
        # 选中行数据的text属性--该属性在放置数据时候,填充的是主键值
        dataId = tree.item(curItem).get("text")
        print(f"选中行的id是{dataId}")
        # 删除数据
        msg="删除成功!" if fs.deleteById(dataId) else "删除失败"
        tips.set(str(msg))
        # 重新检索
        bc.showDataTree(tree, fs.queryFilm())
    tree.bind('<Double-1>', delrow)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    row1.pack()

    bc.newEmptyRow(win)  # -------------分割线--------------

    # 编辑第一行的控件
    row2 = tk.Frame(win)
    fno = bc.newEntry(row2, '影片编号:')
    fname = bc.newEntry(row2, '         影片名称:')
    bc.newLabel(row2, "    ")

    tips = tk.StringVar()
    tips.set("")

    def addFilm():
        # 添加影片
        msg = '添加成功!' if fs.addFilm(fno.get(), fname.get()) else '添加失败'
        # 查询影片并显示结果
        bc.showDataTree(tree, fs.queryFilm())
        tips.set(str(msg))

    ttk.Button(row2, text='  添加  ', command=addFilm).pack(side='left')

    row2.pack()
    row3 = tk.Frame(win)
    TipLabel = tk.Label(row3, textvariable=tips)
    TipLabel.pack(side="left")
    row3.pack()
    # 查询数据,显示结果
    bc.showDataTree(tree, fs.queryFilm())

    def closeThis():
        # #销毁当前窗口
        win.destroy()
        # #打开主窗口
        mw.openWindow()

    # 添加事件拦截方法
    win.protocol("WM_DELETE_WINDOW", closeThis)
    win.mainloop()


if __name__ == '__main__':
    openWindow()
