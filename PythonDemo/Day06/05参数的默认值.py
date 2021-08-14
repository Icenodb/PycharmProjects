"""
默认值参数的注意事项
1.默认值必须为与参数列表的最后
2.如果多个参数都有默认值，那么这些默认值参数，都需要位于参数列表的右侧，顺序随意
"""


def openWindow(title: str, bgColor: str, width: int = 480, height: int = 200):
    win_info = f"即将创建一个窗口,标题为{title},该窗口背景色为{bgColor},"
    win_info += f"窗口的大小是{width}x{height}"
    print(win_info)


if __name__ == "__main__":
    # #以默认值创建窗口
    # openWindow('员工管理','#FFF')
    # #以指定尺寸,重建窗口
    # openWindow('员工管理','#FFF',800,400)

    # 混合调用:titile传值,bgColor传值,然后宽度采用默认值,高度采用自定义值
    openWindow('员工管理', '#78f0f4', height=100)
