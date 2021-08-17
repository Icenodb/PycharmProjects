import sqlite3


def initDb():
    """
    1.连接到目标数据库上
    """
    # 连接到目标数据库,如果数据库不存在,则会自动创建数据库

    conn = sqlite3.connect("test.db")
    conn.close()


if __name__ == "__main__":
    initDb()
    print("--------end---------")
