# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:55:58 2021

@author: wangxg
"""

# import re

# it = re.finditer(r"\d+","12a32bc4322jf3")
# for match in it:
#     print (match.group() )


import jieba

strText="我来自xxx大学,我的实验室在xxxx"
"""
cut  -- 切词,提取词语
cut_all  False, 精准模式,是默认值
         True   全模式
"""
words=jieba.cut(strText)
print(list(words))

words=jieba.cut(strText,cut_all=True)
print(list(words))





