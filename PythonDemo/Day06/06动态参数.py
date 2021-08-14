def showEmpInfo(ename: str, *alias: list):
    print(f"{ename}的外号为{alias}")


def showEmp(**empInfo):
    print(empInfo)


def addEmp(*paramVal, **dbinfo):
    print(paramVal)
    print(dbinfo)


def showList(*data):
    for e in data:
        print(f"data[{data.index(e)}]={e}")


if __name__ == "__main__":
    showEmpInfo("啊这", *("阿哲", "啊这！", "啊这！！"))
    showEmp(ename="啊这", eid="1001", sex="男")
    addEmp("济南屁王", "男", "汉族", url="localhost", dbname="db01")
    showList(1, 2, 3, 4, 5, 6, 7, 8, 9)
