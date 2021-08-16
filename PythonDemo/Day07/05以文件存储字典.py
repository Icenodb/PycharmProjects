import random


def createEmp():
    """
    创建数据
    """
    with open("emp.db", "w", encoding="utf-8") as fw:  # 这样打开文件不用自己关闭 懒鬼福音
        for eid in range(1, 31):
            empInfo = {
                "eid": eid,
                "ename": "员工" + str(eid),
                "sex": "男" if random.randint(1, 100) % 2 else "女",
                "sal": round(random.uniform(8000, 9000), 2)  # 指定小数两位
            }
            fw.write(str(empInfo) + "\n")


def upNumber(num: float):
    """四舍五入"""
    return float(f"{num:.2f}")


def modifyById(eid: int, *data):
    """
    按主键值进行修改
    :param eid: 主键值
    :param data: 修改的数据
    """
    # 打开数据库文件
    with open("emp.db", "r", encoding="utf-8") as fr:
        rows = fr.readlines()
        # 拼接查询条件
        qstr = f"'eid': {eid},"
        for row in rows:
            print(qstr, "#", row.find(qstr), "#", row)
            if row.find(qstr) + 1:
                # 如果找到则为1,此时为True,如果找不到为-1,加1之后为0,False
                index = rows.index(row)
                row_dict = eval(row)  # 将当前行数据转换为字典
                # 修改数据
                row_dict["ename"] = data[0]
                row_dict["sex"] = data[1]
                row_dict["sal"] = round(data[2], 2)
                # 将当前行数据修改
                rows[index] = str(row_dict) + "\n"
                break
    # 将修改后的内容,重新写回到文件中
    with open('emp.db', 'w', encoding='utf-8') as fw:
        fw.write("".join(rows))


if __name__ == "__main__":
    # createEmp()
    modifyById(10, '杜甫', '男', 6789.4567)
    print("-----end----")
