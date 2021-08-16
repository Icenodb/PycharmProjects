import random

"""
作业:重构数据库作业,
可以完成键盘输入数据的录入,
指定id值的修改,指定id值的删除,
以及指定一批id然后批量删除
"""
db = {}
rows = list()
lable = {"a": "address", "p": "phone", "s": "sex"}


def createEmp():
    """
    创建数据
    """
    with open("作业_数据库.db", "w", encoding="utf-8") as fw:  # 这样打开文件不用自己关闭 懒鬼福音
        for eid in range(1, 31):
            empInfo = {
                "eid": eid,
                "ename": "员工" + str(eid),
                "sex": "男" if random.randint(1, 100) % 2 else "女",
                "sal": round(random.uniform(8000, 9000), 2)  # 指定小数两位
            }
            fw.write(str(empInfo) + "\n")


def getDb():
    """
    获取本地文件中的数据，返回字典
    :return rows字典
    """
    with open("作业_数据库.db", "r", encoding="utf-8") as fr:
        rows = fr.readlines()
        return rows


def writeDb(db: list):
    """
    :param db: 传入的list数据
    写入本地文件
    """
    with open('作业_数据库.db', 'w', encoding='utf-8') as fw:
        fw.write("".join(db))


def hasEmpId(eid: int):
    """

    :param eid: 查询eid
    :return: 如果有则返回字典数据，否则为None
    """
    rows = getDb()
    # 拼接查询条件
    qstr = f"'eid': {eid},"
    for row in rows:
        if row.find(qstr) + 1:
            dict_row = eval(row)
            return dict_row
    return None


def hasEmpName(ename: str):
    """

    :param ename: 查询ename
    :return: 如果有则返回字典数据，否则为None
    """
    rows = getDb()
    # 拼接查询条件
    qstr = f"'ename': '{ename}',"
    for row in rows:
        if row.find(qstr) + 1:
            dict_row = eval(row)
            return dict_row
    return None


def modifyById(eid: int, data: dict):
    """
    按主键值进行修改
    :param eid: 主键值
    :param data: 修改的数据
    """
    # 打开数据库文件
    rows = getDb()
    # 拼接查询条件
    qstr = f"'eid': {eid},"
    # 如果找到则为1,此时为True,如果找不到为-1,加1之后为0,False
    for row in rows:
        if row.find(qstr) + 1:
            if data is None:
                index = rows.index(row)
                print(row)
                rows[index] = str("")
                #清空行数据
                break

            else:
                index = rows.index(row)
                row_dict = eval(row)  # 将当前行数据转换为字典
                # 修改数据
                row_dict["ename"] = data["ename"]
                row_dict["sex"] = data["sex"]
                row_dict["sal"] = round(float(data["sal"]), 2)
                # 将当前行数据修改
                rows[index] = str(row_dict) + "\n"
                break
    # 将修改后的内容,重新写回到文件中
    writeDb(rows)


# 添加员工的方法
def addEmp():
    """
    添加员工
    -->传入一个字典类型的数据
    输入员工姓名
    输入e或者直接回车 退出函数
    检查是否存在这个员工
    不存在则继续输入员工的信息(电话号码,住址,性别)，以英文逗号间隔
    """
    while True:
        rows = getDb()
        ename = input("请输入要添加的员工的姓名:")
        if ename.lower() == "e" or ename == "":
            break
        dict_row = hasEmpName(ename)
        if dict_row:
            print(f"员工{ename}已存在")
            continue
        else:
            empInfo = input("请输入员工的信息(性别,薪资):")
            listInfo = empInfo.split(",")
            emp = {
                "eid": len(rows) + 1,
                "ename": ename,
                "sex": listInfo[0],
                "sal": round(float(listInfo[1]), 2)
            }
            rows.append(str(emp) + "\n")
            writeDb(rows)
            print("添加完成")
            print("=======================================")


# 查询员工的方法
def queryEmp():
    """
    查询员工
    -->传入一个字典类型的数据
    输入员工姓名
    输入e或者直接回车 退出函数
    检查是否存在这个员工
    如存在则输出该员工相关数据
    """
    while True:
        rows = getDb()
        tag = True
        eid = input("请输入要查询的员工的id:")
        if eid.lower() == "e" or eid == "":
            break
        dict_row = hasEmpId(eid)
        if dict_row:
            print(f"员工的姓名:{dict_row['ename']}")
            print(f"员工的性别:{dict_row['sex']}")
            print(f"员工薪资:{dict_row['sal']}")

        else:
            print("该员工不存在\n")
            break


# 更新员工信息的方法
def updateEmp():
    """
       更新员工
       -->传入一个字典类型的数据
       输入员工姓名
       输入e或者直接回车 退出函数
       检查是否存在这个员工
       如存在则输入修改后的数据(电话号码,住址,性别),以英文逗号间隔
       """
    while True:
        eid = input("请输入要更新信息的员工的id:\n")
        if eid.lower() == "e" or eid == "":
            break
        dict_row = hasEmpId(eid)
        print(dict_row)
        if dict_row:
            print(f"员工'{eid}'的信息如下:")
            print(f"员工姓名:{dict_row['ename']}")
            print(f"员工性别:{dict_row['sex']}")
            print(f"员工薪资:{dict_row['sal']}")
            empInfo = input("请输入修改后的信息(姓名,性别,薪资):")
            listInfo = empInfo.split(",")
            dict_row['ename'] = listInfo[0]
            dict_row['sex'] = listInfo[1]
            dict_row['sal'] = listInfo[2]
            print(dict_row)
            modifyById(eid, dict_row)
            print("修改成功")
            break
        else:
            print("此员工不存在")


# 删除员工
def delEmp():
    """
    删除员工
       -->传入一个字典类型的数据
       输入员工姓名
       输入e或者直接回车 退出函数
       检查是否存在这个员工
       如存在直接删除
    """
    while True:
        eid = input("请输入要删除的员工的id:\n")
        if eid.lower() == "e" or eid == "":
            break
        eids = eid.split(",")
        for e in eids:
            modifyById(int(e), None)


if __name__ == '__main__':

    while True:

        # print(getDb())
        option = input("请选择要进行的操作\n"
                       "A:添加员工\n"
                       "B:查询员工\n"
                       "C:更新员工信息\n"
                       "D:删除员工\n"
                       "E:退出\n")
        if option.lower() == "a":
            addEmp()
            print("=======================================")
        elif option.lower() == "b":
            queryEmp()
            print("=======================================")
        elif option.lower() == "c":
            updateEmp()
            print("=======================================")
        elif option.lower() == "d":
            delEmp()
            print("=======================================")
        elif option.lower() == "e" or option == "":
            print("感谢使用\n")
            print("=======================================")
            break

    # modifyById(10, '杜甫', '男', 6789.4567)
    # print("-----end----")
