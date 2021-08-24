import urllib

import requests

url = 'https://accounts.douban.com/j/mobile/login/basic'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
    'Origin': 'https://accounts.douban.com',
    'content-Type': 'application/x-www-form-urlencoded',
    'x-requested-with': 'XMLHttpRequest',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'connection': 'keep-alive'
    , 'Host': 'accounts.douban.com'
}
data = {
    'ck': '',
    'name': '',
    'password': '',
    'remember': 'false',
    'ticket': ''
}


def login():
    """
    读取账号密码的配置文件并格式化为请求
    :return: cookies
    """
    with open("loginProperties.txt", "r", encoding="utf-8") as fr:
        properties = fr.readlines()
        for row in properties:
            pt_dict = eval(row)
    data = pt_dict
    data = urllib.parse.urlencode(data)
    req = requests.post(url, headers=header, data=data, verify=False)
    cookies = requests.utils.dict_from_cookiejar(req.cookies)
    return cookies


if __name__ == "__main__":
    print()
    login()
