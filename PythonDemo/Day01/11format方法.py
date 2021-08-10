
first="X"
center="0000"
last="15"
# txt="员工编号以{}开头,以格式串{}填充,以流水号结尾,例如{}".format(first,center,last)
#此处基于索引绑定,完成数据替换,大括号的索引从0开始
txt="员工编号以{}开头,以格式串{}填充,以流水号结尾,例如{}"
txt=txt.format(first,center,last)
print(txt)

ename="杜甫"
eno="1001"
tag="1"
empinfo="""
员工{0}的信息如下:
姓名{0},员工编号{1},性别{2},状态{2},民族{2}
""".format(ename,eno,tag)
print(empinfo)

#format方法的缺陷
#{} 是字符串的一部分
# str1="对于等式{x+y=z},来说,当x和y的值都是正数,此时z一定大于0"
# print(str1)
x=10
y=20
str1="对于等式{{x+y=z}},来说,当x={},y的值={},此时z={}"
print(str1.format(x,y,x+y))

str1="对于等式{}x+y=z{}，来说，当x={}，y的值={}，此时z={}"
print(str1.format("{","}",x,y,x+y))