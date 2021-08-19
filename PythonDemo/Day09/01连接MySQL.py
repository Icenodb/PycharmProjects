import pymysql
import ast

from Day09 import tools


def getConnection():
    with open("DBOptions.txt", "r", encoding="utf-8") as fr:
        dbinfo = ast.literal_eval(fr.read())
    conn = pymysql.Connection(**dbinfo, cursorclass=pymysql.cursors.DictCursor)
    return conn


def addUser(dto: dict):
    """单一表用户添加"""
    sql = """
    insert into emp(ename,birthday,sex,job,sal)
    values (%s,str_to_date(%s,'%%Y-%%m-%%d'),%s,%s,%s)
    """
    args = [dto['ename'], dto['birthday'], dto['sex'], dto['job'], tools.strToNumber(dto['sal'])]
    tag = False
    with getConnection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, args)
            conn.commit()
            tag = True
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def addEmpAndLog(dto: dict):
    """数据级联添加"""
    sql1 = """
        insert into emp(ename,birthday,sex,job,sal)
        values (%s,str_to_date(%s,'%%Y-%%m-%%d'),%s,%s,%s)
    """
    args1 = [dto['ename'], dto['birthday'], dto['sex'], dto['job'], tools.strToNumber(dto['sal'])]
    sql2 = """
    insert into emplog(bdate,edate,job,sal,eid)
    values(current_date,null,%s,%s,%s)
    """
    tag = False
    with getConnection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql1, args1)
            eno = cursor.lastrowid

            cursor.execute(sql2, [dto['job'], tools.strToNumber(dto['sal']), eno])
            conn.commit()
            tag = True
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def batchAddEmp():
    """读取控制台数据录入db"""
    sql = """
    insert into emp(ename,birthday,sex,job,sal)
        values (%s,str_to_date(%s,'%%Y-%%m-%%d'),%s,%s,%s)
    """
    args = []
    while True:
        info = input("请输入ename,birthday,sex,job,sal:")
        if not info:
            break
        args.append(info.split(','))
        tag = False
        with getConnection() as conn:
            try:
                cursor = conn.cursor()
                cursor.executemany(sql, args)
                conn.commit()
                tag = True
            except Exception as ex:
                print(ex)
                conn.rollback()
        return tag


def deleteById(uid: int):
    """单一实例删除"""
    sql = "delete from emp where eid=%s"
    tag = False
    with getConnection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, [uid])
            conn.commit()
            tag = True
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def deleteEmpAndLog(eid: int):
    """数据的级联删除，先删从表再删主表"""
    sql1 = "delete from emplog where eid=%s"
    sql2 = "delete from emp where eid=%s"
    tag = False
    with getConnection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql1, [eid])
            cursor.execute(sql2, [eid])
            conn.commit()
            tag = True
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def batchDeleteEmp(eidlist: list):
    """按主键列表删除一批数据"""
    sql = "delete from emp where eid=%s"
    args = [[eid] for eid in eidlist]
    tag = False
    with getConnection() as conn:
        try:
            cursor = conn.cursor()
            cursor.executemany(sql, args)
            conn.commit()
            tag = True
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def batchDeleteEmpAndLog(eidlist: list):
    """多表批量删除"""
    sql1 = "delete from emplog where eid=%s"
    sql2 = "delete from emp where eid=%s"
    args = [[eid] for eid in eidlist]
    tag = False
    with getConnection() as conn:
        try:
            cursor = conn.cursor()
            cursor.executemany(sql1, args)
            cursor.executemany(sql2, args)
            conn.commit()
            tag = True
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def addMoney(eid: int, money: float):
    """员工加薪，只修改员工表"""
    sql = "update emp set sal=sal+%s where eid=%s"
    args = [tools.strToNumber(str(money)), eid]
    tag = False
    with getConnection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, args)
            conn.commit()
            tag = True
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def findById(eid: int):
    """单一实例查询"""
    sql = """
    select eid,ename,sex,job,cast(sal as char)sal,
    date_format(birthday,'%%Y-%%m-%%d') birthday
    from emp where eid=%s
    """
    with getConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, [eid])
        row = cursor.fetchone()
    return row


def findByIdForTuple(eid: int):
    """单一实例查询(基于元组封装结果)"""
    sql = """
    select eid,ename,sex,job,cast(sal as char)sal,
    date_format(birthday,'%%Y-%%m-%%d') birthday
    from emp where eid=%s
    """
    with pymysql.Connection(host='localhost', user='root',
                            password='lwh123', database='pydb') as conn:
        cursor = conn.cursor()
        cursor.execute(sql, [eid])
        return cursor.fetchone()


def queryAll():
    """数据批量查询(查询全部)"""
    sql = """
    select eid,ename,sex,job,cast(sal as char)sal,
    date_format(birthday,'%%Y-%%m-%%d') birthday
    from emp limit 5
    """
    with getConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


def AddMoneyAndLog(eid: int, money: float):
    """员工加薪，级联修改"""
    rows=findByIdForTuple(eid)
    args2=[rows[3],rows[4],eid]
    print(rows)
    print(rows[3])
    print(rows[4])

    sql1 = "update emplog set edate=current_date where eid=%s"
    sql2 = "update emp set sal=sal+%s where eid=%s"
    sql3 = """
    insert into emplog(bdate,edate,job,sal,eid)
    values(current_time,null,%s,%s,%s)
    """

    args = [tools.strToNumber(str(money)), eid]
    tag = False
    with getConnection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql1, eid)
            cursor.execute(sql2,args)
            cursor.execute(sql3,args2)
            conn.commit()
            tag = True
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag

# ===================MySQL连接===================
# conn = getConnection()
# print(conn)

# ===================添加员工信息表===================
# dto = dict(ename='员工', birthday='1978-1-1', sex='男', job='架构师', sal='123456.78')
# tag = addUser(dto)
# print(tag)

# ===================(数据级联添加)录入员工同时录入日志===================
# dto = dict(ename='员工', birthday='1978-1-1', sex='男', job='架构师', sal='123456.78')
# tag = addEmpAndLog(dto)
# print(tag)

# ===================数据批量添加===================
# print(batchAddEmp())

# ===================单一实例删除==================
# print(deleteById(1))
# ===================单一实例查询==================
# print(findById(2))
# ===================单一实例查询(基于元组封装结果)==================
# ins=findByIdForTuple(2)
# print(ins)
# ===================数据批量查询==================
# print(queryAll())

# ===================关联方数据修改==================
print(AddMoneyAndLog(4,3000))