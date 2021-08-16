def openFile():
    """
    打开目标文件
    如果文件存在的话,直接打开,不存在则会自动创建一个文件,然后再打开
    w  覆盖写入
    a  append 追加模式
    """
    fw = open("f1.txt", "w", encoding="utf-8")
    while 1:
        info = input("请输入数据:")
        if not info:
            break
        fw.write(info + "\n")  # 将输入文件写入目标文件中
    fw.close()  # 销毁文件流


def openFile2(fileName: str, model: str = "w"):
    f = open(fileName, model)
    while 1:
        info = input("请输入数据:")
        if not info:
            break
        f.write(info + "\n")  # 将输入内容写入目标文件中

    f.close()  # 销毁文件流


if __name__ == "__main__":
    openFile2("f3.txt", "a")
    # openFile2(r"c:\Users\xxx\Documents\Box\f3.txt", "a")
    print("end")
