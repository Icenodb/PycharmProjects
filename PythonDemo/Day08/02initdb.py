import sqlite3

dbname = "test.db"


def createTables():
    """
    读取tableList,自动为数据库建表
    """
    with sqlite3.connect(dbname) as conn:
        with open("tableList.txt", "r", encoding="utf-8") as ftable:
            for baseName in ftable:
                # 拼接表名
                tableName = baseName.replace("\n", "")
                with open(tableName+".sql", "r", encoding="utf-8") as fsql:
                    sql = fsql.read()
                    conn.execute(sql)


if __name__ == "__main__":
    createTables()
    print("---end---")
