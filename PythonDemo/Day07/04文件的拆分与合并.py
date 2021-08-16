def splitFile():
    """
    文件的拆分(按字符)
    """
    # 定义 f0 用来装载偶数位字符
    f0 = open("f0.txt", "w", encoding="utf-8")
    # 定义 f1 用来装载奇数位字符
    f1 = open("f1.txt", "w", encoding="utf-8")
    # 定义 f2 作为读取的源文件
    f2 = open("f2.txt", "r", encoding="utf-8")
    txt = f2.read()
    # 将源文件读取为字符串 并计算长度
    length = len(txt)
    for index in range(0, length):
        if index % 2 == 0:
            f0.write(txt[index])
        else:
            f1.write(txt[index])
    f0.close()
    f1.close()
    f2.close()


def joinFile():
    """
    文件的合并
    """
    # 定义 f2 表示文件合并后的对象
    f2 = open("f2.txt", "w", encoding="utf-8")
    # 定义 f0 表示偶数位源文件
    f0 = open("f0.txt", "r", encoding="utf-8")
    # 定义 f1 表示奇数位源文件
    f1 = open("f1.txt", "r", encoding="utf-8")
    f0list = list(f0.read())
    f1list = list(f1.read())
    # 计算总的长度
    length = len(f0list) + len(f1list)
    for index in range(0, length):
        if index % 2 == 0:  # 偶数位
            f2.write(f0list.pop(0))
        else:  #奇数位
            f2.write(f1list.pop(0))
    f0.close()
    f1.close()
    f2.close()


if __name__ == "__main__":
    # splitFile()
    joinFile()