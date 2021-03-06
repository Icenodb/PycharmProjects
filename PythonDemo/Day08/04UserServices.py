from Day09 import tools as t
import sqlite3

dbname = "az.db"


def addUser(dto: dict = {}):
    """添加员工"""
    sql = "insert into user(name,sex,nation,currjob,sal,memo)"
    sql += "         values(?,?,?,?,?,?)"
    params = [
        dto["name"],
        dto["sex"],
        dto["nation"],
        dto["job"],
        t.strToNumber(dto["sal"]),
        dto.get("memo")  # 这里使用get,原因是如果没有输入的话使其为空而不为Null
    ]
    with sqlite3.connect(dbname) as conn:
        tag = False
        try:
            conn.execute(sql, params)
            conn.commit()
            tag = True
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def batchAddUser():
    """将控制台录入数据，填充到user表中"""
    sql = "insert into user(name,sex,nation,currjob,sal,memo)"
    sql += "         values(?,?,?,?,?,?)"
    params = []
    while 1:
        userInfo = input("请输入用户信息(name,sex,nation,currjob,sal,memo):")
        if not userInfo:
            break
        tem = userInfo.split(",")
        tem[4] = t.strToNumber(tem[4])  # 转换为浮点数
        tem[-1] = None if tem[-1] == '' else tem[-1]
        params.append(tem)
    with sqlite3.connect(dbname) as conn:
        tag = 0
        try:
            conn.executemany(sql, params)
            conn.commit()
            tag = 1
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def deleById(uid: int):
    """按主键删除一条数据"""
    sql = "delete from user where uid=?"
    with sqlite3.connect(dbname) as conn:
        tag = 0
        try:
            conn.execute(sql, [uid])
            conn.commit()
            tag = 1
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def addUserAndLog(dto: dict = {}):
    """添加员工，同时录入职务变更日志信息"""
    sql1 = "insert into user(name,sex,nation,currjob,sal,memo)"
    sql1 += "         values(?,?,?,?,?,?)"
    params1 = [
        dto['name'],
        dto['sex'],
        dto['nation'],
        dto['job'],
        t.strToNumber(dto['sal']),
        dto.get('memo')
    ]
    sql2 = "insert into userlog(bdate,edate,job,sal,uid)"
    sql2 += "            values(current_date,null,?,?,?)"
    params2 = [dto['job'], t.strToNumber(dto['sal'])]
    with sqlite3.connect(dbname) as conn:
        tag = 0
        try:
            uid = conn.execute(sql1, params1).lastrowid
            params2.append(uid)
            conn.commit()
            tag = 1
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


# =================0918=========================
def deleteByIdUserAndLog(uid: int):
    """数据级联删除"""
    sql1 = "delete from userlog where uid=?"
    sql2 = "delete from user where uid=?"
    with sqlite3.connect(dbname) as conn:
        tag = 0
        try:
            conn.execute("PRAGMA foreign_keys=ON")
            conn.execute(sql1, [uid])
            conn.execute(sql2, [uid])
            conn.commit()
            tag = 1
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def batchDeleteUser(idlist: list):
    """数据批量删除"""
    sql = "delete from user where uid=?"
    parameters = [[id] for id in idlist]
    with sqlite3.connect(dbname) as conn:
        tag = 0
        try:
            conn.executemany(sql, parameters)
            conn.commit()
            tag = 1
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def batchDeleteUserAndLog(idlist: list):
    """批量级联删除"""
    sql1 = "delete from userlog where uid=?"
    sql2 = "delete from user where uid=?"
    # 转换主键列表
    params = [[uid] for uid in idlist]
    with sqlite3.connect(dbname) as conn:
        tag = 0
        try:
            conn.execute("PRAGMA foreign_keys=ON")
            conn.executemany(sql1, params)
            conn.executemany(sql2, params)
            conn.commit()
            tag = 1
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


if __name__ == '__main__':
    # idlist=[12,14,16]
    # tag=batchDeleteUser(idlist)
    # print(tag)

    idlist = [1, 3, 5, 7, 9]
    tag = batchDeleteUserAndLog(idlist)
    print(tag)

    # tag=deleteByIdUserAndLog(10)
    # print(tag)

    # for uno in range(1,11):
    #      dto={'name':'员工'+str(uno),'sex':'男','nation':'满族',
    #            'job':'程序员','sal':'23456.789'}
    #      tag=addUserAndLog(dto)
    #      print(tag)

    # dto = {'name': '李白', 'sex': '男', 'nation': '汉族',
    #        'job': '程序员', 'sal': '23456.789'}
    # tag = addUserAndLog(dto)
    # print(tag)

    # tag=addUser(dto)
    # print(tag)
    # msg='添加成功' if batchAddUser() else '添加失败'

    # msg='删除成功!' if deleteById(4) else '删除失败!'
    # print(msg)

    print("end")
