from string import Template

first="X"
center="0000"
last=15
#构造字符串模板
temp=Template("员工信息以$f开头,中间填充一串$c.最后是流水号$l")
#将模板的占位符替换为具体的变量值,以构成字符串
txt=temp.substitute(f=first,c=center,l=last)
print(txt)