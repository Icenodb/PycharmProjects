def readAll(): # 读取全部内容
    with open("f3.txt","r",encoding="utf-8") as fr:
        # 将文件内容整体读取,形成一个字符串
        txt = fr.read()
        print(txt)

def readLine():
    """读取文件的一行"""
    with open('f3.txt', 'r', encoding='utf-8') as fr:
        row = fr.readline()
        print(row)

def readRows1():
    """
    将文件的所有行读取到列表里面
    """
    with open("f3.txt","r",encoding="utf-8") as fr:
        dataList=fr.readlines()
        for row in dataList:
            #获取row在dataList中第一次出现的位置
            index=dataList.index(row)