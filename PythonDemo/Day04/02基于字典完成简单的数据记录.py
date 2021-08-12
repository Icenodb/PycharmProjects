# people={}
# # people['ename']='王兴刚'  #添加键值对
# # people['ename']='郭德纲'  #更新键值对
# # print(people['ename'])   #基于键读取值
# people['王兴刚']={'phone':'110','address':'中国.青岛'}
# people['岳云鹏']={'phone':'50','address':'活着我心中'}
# print(people)  #显示全部数据
# print('-----------------------------------------')
# #显示王兴刚的信息
# print(people['王兴刚'])
# print('-----------------------------------------')
# #获取王兴刚的手机号码
# print(people['王兴刚']['phone'])


# 录入数据
# people={}
# while True:
#     info=input("请输入用户信息:uname,phone,address?")
#     if info.lower()=="q":break
#     list_info=info.split(",")
#     people[list_info[0]]={"phone":list_info[1],"address":list_info[2]}
# print(people)

db = {
    '王兴刚':
        {'phone': '110', 'address': '中国.青岛'},
    '岳云鹏':
        {'phone': '50', 'address': '活着我心中'},
    '毛惊奇':
        {'phone': '119', 'address': '中国.四川.巴中'}
}

lable = {"a": "address", "p": "phone"}
while True:
    uname=input("E请输入姓名:")
    if uname.lower()=="q":break

    if not uname in db:
        print(f"找不到名为'{uname}'的用户")
        continue

    while True:
        key=input(f"请输入'{uname}'的phone(p) 或者address(a):")
        if not key in lable:
            print(f"公民 {uname},没有登记 与{key}相关的信息")
            continue
        else:
            key=lable[key]
            print(f"公民{uname}的{key}信息如下:{db[uname][key]}")
            break
