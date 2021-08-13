score = float(input("请输入成绩:"))
if score > 100:
    print("别扯淡.....")
elif 80 <= score <= 100:
    print("优秀")
elif 70 <= score < 80:
    print("良好")
else:
    print("安慰奖!")
