import sqlite3

dbname = "az.db"


def row_dict_factory(cursor, row):
    """
    重构游标对象的行工厂
    将每行数据,改变为字典封装
    :param cursor: 游标对象
    :param row: 行
    :return: 字典
    """
    tiles = [[tup[0]] for tup in cursor.description]
    ins = {}
    for key, value in zip(tiles, row):
        ins[key] = value
    return ins


def findById(uid: int):
    sql = """
    select x.uid,x.name,x.sex,x.nation,x.currjob,x.sal
    from user x
    where x.uid=?
    """
    with sqlite3.connect(dbname) as conn:
        # 游标对象
        cursor = conn.cursor()
        # 修改cursor的行工厂对象
        cursor.row_factory = row_dict_factory()
        cursor.execute(sql, [uid])
        row = cursor.fetchone()
    return row


def modifyJob(uid: int, newJob: str, addSal: float):
    """修改员工的工资和职务"""
    ins = findById(uid)
    sal = ins['sal'] + addSal  # 新的工资

    # 修改职务,并且加工资
    sql1 = """
       update user
          set currjob=?,sal=?
        where uid=?
    """
    args1 = [newJob, sal, uid]

    # 结束员工原来职务
    sql2 = """
       update userlog
          set edate=current_date
        where edate is null
          and uid=?
    """
    args2 = [uid]

    # 添加新的职务和工资
    sql3 = """
       insert into userlog(uid,bdate,edate,job,sal)
                    values(?,date(current_date,'+1 day'),null,?,?)
    """
    args3 = [uid, newJob, sal]

    with sqlite3.connect(dbname) as conn:
        tag = 0
        conn.execute("PRAGMA foreign_keys=ON")
        try:
            conn.execute(sql1, args1)
            conn.execute(sql2, args2)
            conn.execute(sql3, args3)
            conn.commit()
            tag = 1
        except Exception as ex:
            print(ex)
            conn.rollback()
    return tag


def queryAll():
    sql = """
      select x.uid,x.name,x.sex,x.nation,x.currjob
        from user x
    """
    with sqlite3.connect(dbname) as conn:
        cursor = conn.cursor()
        # cursor.row_factory=row_dict_factory
        cursor.execute(sql)
        return cursor.fetchall()


if __name__ == '__main__':
    # row=findById(3)
    # print(row)
    # modifyJob(3, '项目经理', 10000)
    rows = queryAll()
    print(rows)
