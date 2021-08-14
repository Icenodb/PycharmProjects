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

"""
    当参数列表存在动态参数的时候，最好将动态参数放到参数列表的最后，否则调用的时候，动态参
    数之后的参数，需要按名传参调用，否则无法清晰为每个参数指定明确的值。
    如果一个函数的参数中同时存在元组动态参数和字典动态参数，那么元组动态参数在前，字典动态
    参数在后，否则报错，这个必须注意。
    另外需要注意的是，一般以字典动态参数做最后一个参数
"""

if __name__ == "__main__":
    showEmpInfo("啊这", *("阿哲", "啊这！", "啊这！！"))
    showEmp(ename="啊这", eid="1001", sex="男")
    addEmp("济南屁王", "男", "汉族", url="localhost", dbname="db01")
    showList(1, 2, 3, 4, 5, 6, 7, 8, 9)
