import sqlite3

dbname = "az.db"
tableListInfo = "tableListInfo.txt"


def regTable():
    """注册需要建立表"""
    with open(tableListInfo, "a", encoding="utf-8") as fa:
        while 1:
            tableInfo = input("请输入表(名,含义):")
            if not tableInfo:
                break
            tab_arr = tableInfo.split(",")
            tab_dict = {
                "name": tab_arr[0],
                "cnname": tab_arr[1],
                "state": 0
            }
            # 将表的描述信息,写入目标文件
            fa.write(str(tab_dict) + "\n")


def getTableList():
    """获取所有需要创建的表的名称(即state为0)"""
    sqlFileList = []
    with open(tableListInfo, "r", encoding="utf-8") as flist:
        tableList = flist.readlines()
        for tableInfo in tableList:
            tab_dict = eval(tableInfo)
            if not tab_dict["state"]:  # state为0取反后即为True，此时进入创建流程
                sqlFileName = tab_dict["name"] + ".sql"  # 文件名称
                sqlFileList.append(sqlFileName)
                tab_dict["state"] = 1
                index = tableList.index(tableInfo)
                tableList[index] = str(tab_dict) + "\n"
    return sqlFileList, tableList


def creatTable():
    """为数据库创建所有状态为0的表(应存在对应的建表.sql文件)"""
    sqlFileList, tabStatelist = getTableList()
    with sqlite3.connect(dbname) as conn:
        for sqlFileName in sqlFileList:
            with open(sqlFileName, "r", encoding="utf-8") as fsql:
                sqlStmt = fsql.read()
                conn.execute(sqlStmt)
    with open(tableListInfo, "w", encoding="utf-8") as fw:
        fw.write("".join(tabStatelist))


if __name__ == "__main__":
    # regTable()
    # creatTable()
    print("===end===")
