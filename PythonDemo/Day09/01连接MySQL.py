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


dto = dict(ename='员工', birthday='1978-1-1', sex='男', job='架构师', sal='123456.78')
tag = addUser(dto)
print(tag)

conn = getConnection()
print(conn)
