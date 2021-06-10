
# 1/直接in字典,能获取k
dict1 = {'case1': '1', 'case2': '2'}
for k in dict1:
    print(k)
'''
case1
case2
'''
print("********")

# 2/效果同上,in字典的keys()能获取k
for k in dict1.keys():
    print(k)
'''
case1
case2
'''
print("********")

# 3/单个变量获取到items的元组
for k in dict1.items():
    print(k)
    print(type(k))  # <class 'tuple'>
'''
('case1', '1')
('case2', '2')
'''
print("********")

# 4/标准用法
for k, v in dict1.items():
    print(k)
    print(v)
'''
case1
1
case2
2
'''

# 5/
print(dict1.items())  # dict_items([('case1', '1'), ('case2', '2')])
'''# 字典的items方法，以列表返回可遍历的(键, 值) 元组数组'''
print(type(dict1.items()))  # <class 'dict_items'>
