db = {}
lable = {"a": "address", "p": "phone", "s": "sex"}


# 添加员工的方法
def addEmp(db: dict):
    while True:
        uname = input("请输入要添加的员工的姓名:")
        if uname.lower() == "c": break
        if uname in db:
            print("该员工已经存在\n")
            print("=======================================")
            continue
        else:
            empInfo = input("请输入员工的信息(电话号码,住址,性别):")
            listInfo = empInfo.split(",")
            db[uname] = {"phone": listInfo[0], "address": listInfo[1], "sex": listInfo[2]}
            break


# 查询员工的方法
def queryEmp(db: dict):
    while True:
        uname = input("请输入要查询的员工的姓名:")
        if uname.lower() == "c": break
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

def updateEmp(db:dict,uname:str):
    print()

if __name__ == '__main__':
    while True:
        option = input("请选择要进行的操作\n"
                       "A:添加员工\n"
                       "B:查询员工\n"
                       "C:退出\n")
        if option.lower() == "a":
            addEmp(db)
            print(db)
            print("=======================================")
        elif option.lower() == "b":
            queryEmp(db)
            print("=======================================")
        elif option.lower() == "c":
            print("感谢使用\n")
            print("=======================================")
            break
