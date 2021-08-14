import json

db = {}
lable = {"a": "address", "p": "phone", "s": "sex"}


# 将字典转换为json保存
def toJson(db: dict):
    """
    -->db:dict传入一个字典
    <--将字典写入到db.json文件中
    """
    json_str = json.dumps(db, indent=4)
    with open('db.json', 'w') as json_file:
        json_file.write(json_str)


# 将json读取为字典
def toDict():
    """
    <--读取db.json文件并返回字典类型的数据
    """
    with open('db.json', 'r') as f:
        return json.load(fp=f)


# 添加员工的方法
def addEmp(db: dict):
    """
    添加员工
    -->传入一个字典类型的数据
    输入员工姓名
    输入e或者直接回车 退出函数
    检查是否存在这个员工
    不存在则继续输入员工的信息(电话号码,住址,性别)，以英文逗号间隔
    """
    while True:
        uname = input("请输入要添加的员工的姓名:")
        if uname.lower() == "e" or uname == "": break
        if uname in db:
            print("该员工已经存在\n")
            print("=======================================")
            continue
        else:
            empInfo = input("请输入员工的信息(电话号码,住址,性别):")
            listInfo = empInfo.split(",")
            db[uname] = {"phone": listInfo[0], "address": listInfo[1], "sex": listInfo[2]}
            toJson(db)
            break


# 查询员工的方法
def queryEmp(db: dict):
    """
    查询员工
    -->传入一个字典类型的数据
    输入员工姓名
    输入e或者直接回车 退出函数
    检查是否存在这个员工
    如存在则输出该员工相关数据
    """
    while True:
        uname = input("请输入要查询的员工的姓名:")
        if uname.lower() == "e" or uname == "": break
        if uname not in db:
            print(f"没有员工'{uname}'的相关信息\n")
            print("=======================================")
            continue
        else:
            print(f"该员工'{uname}'的信息如下:\n")
            print(f"员工电话:{db[uname]['phone']}\n")
            print(f"员工住址:{db[uname]['address']}\n")
            print(f"员工性别:{db[uname]['sex']}\n")
            print()


# 更新员工信息的方法
def updateEmp(db: dict):
    """
       更新员工
       -->传入一个字典类型的数据
       输入员工姓名
       输入e或者直接回车 退出函数
       检查是否存在这个员工
       如存在则输入修改后的数据(电话号码,住址,性别),以英文逗号间隔
       """
    while True:
        uname = input("请输入要更新信息的员工的姓名:\n")
        if uname.lower() == "e" or uname == "": break
        if uname not in db:
            print(f"该员工'{uname}'不存在\n")
            continue
        else:
            print(f"该员工'{uname}'的信息如下:\n")
            print(f"员工电话:{db[uname]['phone']}\n")
            print(f"员工住址:{db[uname]['address']}\n")
            print(f"员工性别:{db[uname]['sex']}\n")
            empInfo = input("请输入修改后的信息(电话号码,住址,性别):")
            listInfo = empInfo.split(",")
            db[uname] = {"phone": listInfo[0], "address": listInfo[1], "sex": listInfo[2]}
            toJson(db)
            break


#删除员工
def delEmp(db: dict):
    """
    删除员工
       -->传入一个字典类型的数据
       输入员工姓名
       输入e或者直接回车 退出函数
       检查是否存在这个员工
       如存在直接删除
    """
    while True:
        uname = input("请输入要删除的员工的姓名:\n")
        if uname.lower() == "e" or uname == "": break
        if uname not in db:
            print(f"该员工'{uname}'不存在\n")
            continue
        else:
            del db[uname]
            toJson(db)


if __name__ == '__main__':
    while True:
        db = toDict()
        print(db)
        option = input("请选择要进行的操作\n"
                       "A:添加员工\n"
                       "B:查询员工\n"
                       "C:更新员工信息\n"
                       "D:删除员工\n"
                       "E:退出\n")
        if option.lower() == "a":
            addEmp(db)
            print(db)
            print("=======================================")
        elif option.lower() == "b":
            queryEmp(db)
            print("=======================================")
        elif option.lower() == "c":
            updateEmp(db)
            print("=======================================")
        elif option.lower() == "d":
            delEmp(db)
            print("=======================================")
        elif option.lower() == "e" or option == "":
            print("感谢使用\n")
            print("=======================================")
            break
