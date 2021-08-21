import sqlite3 as s3

sql = """
insert into syscode(fname,fcode,fvalue,isv)
     values(?,?,?,?)
"""
args = []

with open('nation.txt', 'r', encoding='utf-8') as fr:
    for row in fr:
        option = row.split(':')
        val = ['nation', option[0], option[1], '1']
        args.append(val)

with s3.connect("../Day08/az.db") as conn:
    tag = False
    try:
        conn.executemany(sql, args)
        conn.commit()
        tag = True
    except Exception as ex:
        print(ex)
        conn.rollback()

print(tag)
