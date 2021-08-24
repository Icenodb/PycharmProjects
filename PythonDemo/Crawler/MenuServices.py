import os
import sqlite3
import tkinter as tk
import FilmWindow as fw
import baseContr as bc
import CommentWindow as cw

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

    dataMenu.add_command(label="数据库初始化", command=createTable)

    def filmsManager():
        mainWin.destroy()
        fw.openWindow()

    def commentManager():
        mainWin.destroy()
        cw.openWindow()

    dataMenu.add_command(label='影片管理', command=filmsManager)
    mainMenu.add_cascade(label='数据维护', menu=dataMenu)
    commentMenu = tk.Menu(tearoff=0)
    commentMenu.add_command(label='短评管理',command=commentManager)
    mainMenu.add_cascade(label='短评管理', menu=commentMenu)
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
