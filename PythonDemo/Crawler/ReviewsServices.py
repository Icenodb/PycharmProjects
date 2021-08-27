import re
import sqlite3
from bs4 import BeautifulSoup
import requests

from Crawler.login import login

dbname = 'douban.db'


def addReviews(fno: str, uname: str, star: str, content: str, votes: int):
    sql = """
    insert into reviews(fno,uname,star,content,votes) values (?,?,?,?,?)
    """
    with sqlite3.connect(dbname) as conn:
        tag = 0
        try:
            conn.execute(sql, [fno, uname, star, content, votes])
            conn.commit()
            tag = 1
        except Exception as ex:
            conn.rollback()
            print(ex)
    return tag;


def coo_regular():
    with open(r'resources\cookies.txt', "r", encoding="utf-8") as fr:
        properties = fr.readlines()
    coo = {}
    for k_v in "".join(properties).split(';'):
        k, v = k_v.split('=', 1)
        coo[k.strip()] = v.replace('"', '')
    print(coo)
    return coo


def getReviews(cookies, mvid, pageNum: int = 5):
    start = 0
    while start < pageNum * 20:
        dataridList = []
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        mvurl = 'https://movie.douban.com/subject/' + str(mvid) + '/reviews?start=' + str(start)
        # 影片的url
        try:
            start += 20
            req = requests.get(mvurl, cookies=cookies, headers=header)  # 获取初始影评页面
            req.raise_for_status()  # 抛出异常
            res = req.text
            soup = BeautifulSoup(res, 'lxml')  # 把这个结构化html创建一个BeautifulSoup对象以此来提取信息
            node = soup.select('.main-bd')  # 每组class均为comment-item，每个mvurl有20条影评
            for var in node:
                datarid = var.select_one('.review-short').get('data-rid')
                dataridList.append(datarid)
            for rid in dataridList:
                url = 'https://movie.douban.com/review/' + str(rid) + '/'
                # 完整影评的url
                print(f"影评的url:{url}")
                req = requests.get(url, cookies=cookies, headers=header)
                req.raise_for_status()
                res = req.text
                soup = BeautifulSoup(res, 'lxml')
                article = soup.select('.article')
                for v in article:
                    # print(v)
                    useful = v.select_one('.useful_count').text.replace("\n", "").split(" ")
                    useless = v.select_one('.useless_count').text.replace("\n", "").split(" ")
                    star = v.select_one('.main-title-hide')
                    review = v.select_one('.review-content').select('p')
                    uname = v.select('span')[1].text
                    # print(uname)
                    # print(review)
                    ResultReview = parse(str(review))
                    print(ResultReview)
                    if star:
                        star = star.text
                    else:
                        star = '-1'
                    print(f"{useful[-3]}觉得有用,{useless[-3]}觉得没用,星数:{star}")
                    useful = useful[-3]
                    addReviews(mvid, uname, star, ResultReview, int(useful))
                    # return 0

        except Exception as ex:
            print(ex)


def parse(text: str):
    # pattern = re.compile(r'<p*?>.*?</p>', re.S)  # 制定规则
    pattern = re.compile(r'<p[\s\S]*?>([\s\S]*?)</p>', re.S)  # 制定规则

    commentIters = re.finditer(pattern, text)
    realReview = []
    for ci in commentIters:
        commText = ci.group()  # 一条短评
        # 提取影评的内容
        cell = re.findall('<p[\s\S]*?>([\s\S]*?)</p>', commText)
        realReview.append("".join(cell))
    txt = "".join(realReview)
    txt = re.sub('<span[\s\S]*?>([\s\S]*?)</span>', '', txt)
    txt = re.sub('<a[\s\S]*?>([\s\S]*?)</a>', '', txt)
    return txt


if __name__ == '__main__':
    cookies = coo_regular()
    getReviews(cookies, 35161768, pageNum=1)
