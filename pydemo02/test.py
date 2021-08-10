# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:12:29 2021

@author: 1FA
"""

from string import Template

# Unix shell格式
first = "x"
center = "0000"
last = 15
temp = Template("以$f开头，中间$c填充，以$l结尾")
txt = temp.substitute(f=first, c=center, l=last)
print(txt)
# print(type(txt))

txt = "以{}开头，中间{}填充，以{}结尾".format(first, center, last)
print(txt)

fibs=[1,1]
for m in range(3,37):
    fibs.append(fibs[-1]+fibs[-2])
count=0
for e in fibs:
    print(f"{e:>10}",end=" ")
    count+=1
    if count==6:
        print()
        count=0