import baseContr as bc
import MenuServices as ms


def openWindow():
    win = bc.newWindow("主窗口")
    # 为主窗口挂接菜单
    ms.initMenu(win)
    win.mainloop()


if __name__ == '__main__':
    openWindow()
