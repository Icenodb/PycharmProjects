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
