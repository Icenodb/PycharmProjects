def killPerson():
    """
    约瑟夫问题
    """
    person = list(range(1, 31))
    formatList(person, 5)

    count = 0
    psum = 0
    while True:
        for e in person:
            if e:
                count += 1
                if count == 9:
                    print(f"第{e}个人被喂鱼")
                    eindex = person.index(e)
                    person[eindex] = 0
                    psum += 1
                    if psum==15:
                        formatList(person,5)
                        return
                    count=0
    print()


def formatList(data: list, count: int):
    """
    格式化列表
    -->一个list和一个参数，list是数据，参数表示多少个才换行
    并格式化打印
    """
    print("--------------------------------------")
    index = 0;
    for p in data:
        print(f"{p:4}", end=",")
        index += 1
        if (index % count == 0): print()
    print("--------------------------------------")


killPerson()
print(killPerson.__doc__)
print(formatList.__doc__)
