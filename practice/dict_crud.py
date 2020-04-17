# coding=utf-8
# 增create删delete改update查retrieve
# 可将任何Python对象用作字典中的值，如number，string，list，dictionary

# Retrieve，字典名['key']
dict1={'case1':'1','case2':'2'}
print('case1=='+dict1['case1'])

# Create，Python不关心键—值对的添加顺序， 而只关心键和值之间的关联关系
dict1['case3']='3'
dict1['case4']='4'
print(dict1)

# 用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时,通常都需要先定义一个空字典。

# Update，直接修改key和value

# Delete，指定字典名和键值
del dict1['case4']
print(dict1)

# 字典的items方法，以列表返回可遍历的(键, 值) 元组数组。
# 字典的keys(),以列表返回所有键
# 字典的values(),以列表返回所有值
print(dict1.items())
print(dict1.keys())
print(dict1.values())

# 遍历：键值，键，值，按序遍历
for k,v in dict1.items():
    print("key:"+k)
    print("value:"+v)

