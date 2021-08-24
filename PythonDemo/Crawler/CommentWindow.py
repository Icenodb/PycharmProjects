import tkinter as tk
import baseContr as bc
import CommentServices as cs
import random
import time

from Crawler.login import login


def openWindow():
    win = bc.newWindow("短评管理")
    initContr(win)
    win.mainloop()


def initContr(win: tk.Tk):
    bc.newEmptyRow(win)
    bc.newEmptyRow(win)  # -----间隔线------------------------

    # 标题行
    row1 = tk.Frame(win)
    bc.newLabel(row1, '短评管理')  # 创建标题
    row1.pack()
    bc.newHr(win)
    bc.newEmptyRow(win)  # -----间隔线------------------------

    row3 = tk.Frame(win)  # 第三行控件
    infoBox = bc.newText(row3, '', w=70, h=14)  # 消息提示的文本框

    bc.newEmptyRow(win)  # -----间隔线------------------------

    row2 = tk.Frame(win)  # 第二行控件
    # 获取影片名称及编号的列表
    fnoList, fnameList = cs.getFilmList()
    # 生成页面显示的影片下拉列表
    filmList = bc.newSelect(row2, fnameList, '影片列表:   ')
    bc.newLabel(row2, "     ")  # 行内间隔

    def getComm():
        """爬取影片短评"""
        # 1.获取影片名称及选中影片的编号
        fname = filmList.get()
        fno = fnoList[filmList.current()]
        cookies = login()
        text = f"正在爬取影片《{fname}》短评.......\n"
        cs.getcomment(cookies, fno, 'h')
        infoBox.insert('end', text)
        infoBox.yview_moveto(1)
        infoBox.update()
        # 模拟用户正常操作,让当前线程停顿随机时间
        # time.sleep(random.random()*3)

    tk.Button(row2, text='  开爬  ', command=getComm).pack()  # 创建按钮

    row2.pack()
    bc.newEmptyRow(win)  # -----间隔线------------------------
    row3.pack()


if __name__ == '__main__':
    openWindow()
