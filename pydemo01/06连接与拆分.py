#列表元素连接
l1=['赵客缦胡缨，吴钩霜雪明。', '银鞍照白马，飒沓如流星。',
    '十步杀一人，千里不留行。', '事了拂衣去，深藏身与名。',
    '闲过信陵饮，脱剑膝前横。', '将炙啖朱亥，持觞劝侯嬴。']
newString='\n'.join(l1)
print(newString)



text='赵客缦胡缨，吴钩霜雪明。\n银鞍照白马，飒沓如流星。\n'
text+='十步杀一人，千里不留行。\n事了拂衣去，深藏身与名。\n'
text+='闲过信陵饮，脱剑膝前横。\n将炙啖朱亥，持觞劝侯嬴。\n'
print(text.split('\n'))
#以\n为单位切割
print(text.splitlines())


str1="this is Python project"
#按指定字符,将字符串拆分成列表--list
list1=str1.split(" ")
print(list1,type(list1))