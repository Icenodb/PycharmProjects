import sqlite3

dbname = 'douban.db'


def deleteById(fid: int):
    print(f"删除主键值为{fid}的电影数据。。。")


def addFilm(fno: str, fname: str):
    """

    :param fno: 电影编号
    :param fname:电影名称
    :return:tag 是否成功
    """
    sql = """
    insert into film(fno,fname) values(?,?)
    """
    with sqlite3.connect(dbname) as conn:
        tag = 0
        try:
            conn.execute(sql, [fno, fname])
            conn.commit()
            tag = 1
        except Exception as ex:
            conn.rollback()
            print(ex)
    return tag;


def queryFilm():
    """
    查询所有的电影
    :return: 结果集
    """
    sql = """
    select fid,fno,fname from film
    """
    with sqlite3.connect(dbname) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
