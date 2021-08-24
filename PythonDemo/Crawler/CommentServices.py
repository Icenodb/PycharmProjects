import sqlite3

from Crawler.login import login
import requests
from bs4 import BeautifulSoup

import xlwt


def addComment(fno:str,uname:str,star:str,content:str,votes:int):
    sql = """
    insert into comments(fno,uname,star,content,votes) values (?,?,?,?,?)
    """
    with sqlite3.connect(dbname) as conn:
        tag = 0
        try:
            conn.execute(sql, [fno, uname,star,content,votes])
            conn.commit()
            tag = 1
        except Exception as ex:
            conn.rollback()
            print(ex)
    return tag;


def getcomment(cookies, mvid, type: str = 'h', pageNum: int = 5):  # 参数为登录成功的cookies(后台可通过cookies识别用户，电影的id)
    start = 0
    w = xlwt.Workbook(encoding='ascii')  # #创建可写的workbook对象
    ws = w.add_sheet('sheet1')  # 创建工作表sheet
    index = 1  # 表示行的意思，在xls文件中写入对应的行数
    while start < pageNum * 20:
        # 模拟浏览器头发送请求
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        try:
            # 拼凑url 每次star加20
            url = 'https://movie.douban.com/subject/' + str(mvid) + '/comments?percent_type=' + type + '&start=' + str(
                start) + '&limit=20&status=P&sort=new_score'
            start += 20
            print(url)
            # 发送请求
            req = requests.get(url, cookies=cookies, headers=header)
            req.raise_for_status()  # 抛出异常
            res = req.text
            soup = BeautifulSoup(res, 'lxml')  # 把这个结构化html创建一个BeautifulSoup对象用来提取信息
            node = soup.select('.comment-item')  # 每组class 均为comment-item  这样分成20条记录(每个url有20个评论)
            for var in node:
                name = var.a.get('title')
                star = var.select_one('.comment-info').select('span')[1].get('class')[0][-2]
                comment = var.select_one('.short').text
                votes = var.select_one('.votes').text
                print(name, star, votes, comment)
                addComment(str(mvid),name,str(star),comment,int(votes))
                # ws.write(index, 0, index)  # 第0列写入 index
                # ws.write(index, 1, name)  # 第1列写入 评论者
                # ws.write(index, 2, star)  # 第2列写入 评星
                # ws.write(index, 3, votes)  # 第3列写入 投票数
                # ws.write(index, 4, comment)  # 第4列写入 评论内容
                index += 1
        except Exception as e:  # 有异常退出
            print(e)
            break


dbname = 'douban.db'


def getFilmList():
    """
    获取影片列表
    :return: 影片编号列表，影片名称列表
    """
    sql = "select distinct fno,fname from film order by fname"
    with sqlite3.connect(dbname) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        fnoList = []
        fnameList = []
    for ins in rows:
        fnoList.append(ins[0])
        fnameList.append(ins[1])
    return fnoList, fnameList


if __name__ == '__main__':
    url = 'https://movie.douban.com/subject/30435124/comments?percent_type=h&limit=20&status=P&sort=new_score'
    cookies = login()
    mvid = input('电影的id为：')
    getcomment(cookies, mvid, 'h')
