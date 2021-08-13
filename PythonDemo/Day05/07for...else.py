'''
1.在for中,如果break没有被执行,就会在循环结束后,
  自动执行与for匹配的else
'''
sc = [80.12, 58.59, 69.5, 67, 88]
#    0      1     2  3   4
for s in sc:
    if s < 60:
        # 获取索引
        index = sc.index(s)
        print(f"在{sc}中,第{index + 1}个元素,不及格")
        # break
else:
    print(f"在{sc}中没有不及格的成绩")
