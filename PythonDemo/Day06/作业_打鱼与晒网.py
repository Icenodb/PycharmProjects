import datetime


def fishOrSun(day1: datetime, day2: datetime):
    day = (day2 - day1).days + 1
    div = day % 5
    msg = "晒网"
    if 1 <= div <= 3:
        msg = "打鱼"
    print(msg)


def fromNowOn():
    # 获取当前日期
    currentDay = datetime.datetime.now().strftime("%Y-%m-%d")
    # 拆分日期元素
    dayli = [int(e) for e in currentDay.split("-")]
    day1 = datetime.date(2000, 1, 1)
    day2 = datetime.date(*dayli)  # 解包
    fishOrSun(day1, day2)


if __name__ == "__main__":
    fromNowOn()
