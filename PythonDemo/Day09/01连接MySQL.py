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
