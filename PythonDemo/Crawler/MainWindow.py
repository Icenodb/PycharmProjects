import baseContr as bc
import MenuServices as ms


def openWindow():
    win = bc.newWindow("豆瓣影评分析", 7)
    ms.initMenu(win)
    win.mainloop()


if __name__ == "__main__":
    openWindow()
