#入口过宽，出口过窄
emp={"eid":"01","ename":"杜甫","sex":"男","nation":"汉族"}
#目标数据结构，如果没有对应的占位符，那么只能凑活用
txt="员工杜甫的信息是:%s"%(emp)
print(txt)

# pi="3.1415926535"
# #方案1的潜在风险,就是可能产生 赋值变量与占位符类型不匹配
# t2="常数pi的值是%f"%(pi)
# print(t2)

first="X"
center="0000"
last=15
eno="编号按如下规律生成:以%s开头，中间填充一串%s，然后以流水号结尾比如%d"
eno=eno%(first,center,last)
print(eno)

# eno="员工编号按如下规律生成:"
# 拼接last会报错,原因在于last不是字符串类型
# eno+="以"+first+"开头,中间填充一串"+center+",然后以流水号结尾比如"+last
# print(eno)