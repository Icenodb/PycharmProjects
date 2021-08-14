
def fun_fibs(n:int):
    """
    :param n:返回斐波那契数列前n个数
    :return:
    """
    fibs=[1,1]
    for m in range(3,n+1):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

def formatFibs(data:list,rowCount:int):
    """
    :param data:传入列表
    :param rowCount:几个数换行
    """
    print("--------------------------------------")
    index = 0;
    for p in data:
        print(f"{p:10}", end=",")
        index += 1
        if (index % rowCount == 0): print()
    print("--------------------------------------")


if __name__ == '__main__':
    fibsList=fun_fibs(36)
    formatFibs(fibsList,6)