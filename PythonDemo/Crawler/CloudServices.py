import sqlite3
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt  # 绘图模块

WC_FONT_PATH = 'C:/Windows/Fonts/simhei.ttf'  # 词云字体
dbname = 'douban.db'

def createReviewWordImage(fno:str,keyCount:int=30):
    comms=getReviewByFno(fno)
    # 结巴切词--词语提取cut_all=True 全模式 cut_all=False 精准模式(默认)
    wordList = jieba.cut(comms, cut_all=False)
    words = " ".join(wordList)  # 将提取的词语连接成字符串,词语间以空格间隔

    # 获取违禁词汇列表
    stopWordsList = getStopWordsList()
    # 实例化词云对象
    cloud = WordCloud(background_color="white",
                      scale=4,
                      max_words=int(keyCount),
                      width=800, height=450,
                      max_font_size=65,
                      random_state=42,
                      stopwords=stopWordsList,
                      font_path=WC_FONT_PATH)
    # 生成词云,词云对象将应用违禁词汇列表,自动对words清洗
    cloud.generate(words)
    # 生成词云图片
    cloudImgName = f"resources\\{fno}.jpg"
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(cloudImgName, dpi=500)
    plt.clf()
    return cloudImgName

def createCommentWordImage(fno: str, keyCount: int = 30):
    """
      生成该影片的词云图片,
      返回图片的存储位置及名称
    """
    """生成词云"""
    # 获取该影片的影评
    comms = getCommentForFno(fno)

    # 结巴切词--词语提取cut_all=True 全模式 cut_all=False 精准模式(默认)
    wordList = jieba.cut(comms, cut_all=False)
    words = " ".join(wordList)  # 将提取的词语连接成字符串,词语间以空格间隔

    # 获取违禁词汇列表
    stopWordsList = getStopWordsList()
    # 实例化词云对象
    cloud = WordCloud(background_color="white",
                      scale=4,
                      max_words=int(keyCount),
                      width=800, height=450,
                      max_font_size=65,
                      random_state=42,
                      stopwords=stopWordsList,
                      font_path=WC_FONT_PATH)
    # 生成词云,词云对象将应用违禁词汇列表,自动对words清洗
    cloud.generate(words)
    # 生成词云图片
    cloudImgName = f"resources\\{fno}.jpg"
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(cloudImgName, dpi=500)
    plt.clf()
    return cloudImgName


def getStopWordsList():
    """生成违禁词汇列表"""
    with open(r'resources\stopWordsList.txt', 'r', encoding='utf-8') as fr:
        return fr.read().splitlines()


def getCommentForFno(fno):
    """按编号获取短评字符串"""
    sql = """
            select group_concat(content)
              from comments
             where fno=?
    """
    with sqlite3.connect(dbname) as conn:
        cursor = conn.cursor()
        cursor.execute(sql, [fno])
    return cursor.fetchone()[0]

def getReviewByFno(fno):
    """按编号获取短评字符串"""
    sql = """
            select group_concat(content)
              from reviews
             where fno=?
    """
    with sqlite3.connect(dbname) as conn:
        cursor = conn.cursor()
        cursor.execute(sql, [fno])
    return cursor.fetchone()[0]

def getFilmList():
    """获取影片列表"""
    # 定义影片编号及名称列表
    fnoList = []
    fnameList = []
    sql = "select distinct fno,fname from film order by fname"
    with sqlite3.connect(dbname) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        # 解析数据,生成列表
        for row in cursor:
            fnoList.append(row[0])
            fnameList.append(row[1])

    return fnoList, fnameList
