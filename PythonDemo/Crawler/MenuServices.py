import tkinter as tk
import FilmWindow as fw
import baseContr as bc
import CommentWindow as cw
import CloudWindow as clw
import sqlite3
import os
import ReviewWindow as rw
import ReviewsCloudWindow as rcw
dbname = "douban.db"


def initMenu(mainWin: tk.Tk):
    # 创建主菜单
    mainMenu = tk.Menu()
    # 数据维护
    dataMenu = tk.Menu(tearoff=0)

    # 读取ScriptList的内容,创建数据库中表---判断建表语句文件是否存在,存在则创建,不存在则忽略

    def createTable():
        with sqlite3.connect(dbname) as conn:
            with open("tableList.txt", "r", encoding="utf-8") as ftable:
                for baseName in ftable:
                    # 拼接表名
                    tableName = baseName.replace("\n", "") + ".sql"
                    if os.access(tableName, os.F_OK):
                        with open(tableName, "r", encoding="utf-8") as fsql:
                            sql = fsql.read()
                            conn.executescript(sql)
        print("初始化成功")

    def filmsManager():
        mainWin.destroy()
        fw.openWindow()

    def commentManager():
        mainWin.destroy()
        cw.openWindow()

    def showCloudWord():
        mainWin.destroy()
        clw.openWindow()

    def reviewManager():
        mainWin.destroy()
        rw.openWindow()

    def reviewCloudManage():
        mainWin.destroy()
        rcw.openWindow()

    dataMenu.add_command(label="数据库初始化", command=createTable)
    dataMenu.add_command(label='影片管理', command=filmsManager)
    mainMenu.add_cascade(label='数据维护', menu=dataMenu)
    commentMenu = tk.Menu(tearoff=0)
    commentMenu.add_command(label='短评爬取', command=commentManager)
    commentMenu.add_command(label='生成词云', command=showCloudWord)
    # mainMenu.add_cascade(label='评论管理', menu=commentMenu)
    commentMenu.add_command(label='认可度分析')
    commentMenu.add_separator()
    commentMenu.add_command(label='评论爬取',command=reviewManager)
    commentMenu.add_command(label='生成词云',command=reviewCloudManage)
    commentMenu.add_command(label='认可度分析')
    mainMenu.add_cascade(label='影评管理', menu=commentMenu)

    commentMenu = tk.Menu(tearoff=0)  # 影片评论管理

    def getComm():
        cw.openWindow()

    # 系统维护
    sysMenu = tk.Menu(tearoff=0)
    sysMenu.add_command(label='口令维护')
    sysMenu.add_separator()  # 一条分割线

    def exitMainWindow():
        # 销毁主窗口
        mainWin.destroy()

    sysMenu.add_command(label='退出', command=exitMainWindow)
    mainMenu.add_cascade(label='系统维护', menu=sysMenu)
    mainWin.config(menu=mainMenu)


if __name__ == "__main__":
    win = bc.newWindow("豆瓣影评分析", 7)
    initMenu(win)
    win.mainloop()
