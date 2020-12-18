# 8种new字典的方法

# 1直接赋值
dict1 = {"key1": "value 1", "key2": "value 2"}

# 23空字典
dict2 = {}
dict3 = dict()

# 4通过zip函数
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(zip(list1, list2))  # <zip object at 0x00591C88>
print(list(zip(list1, list2)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print(tuple(zip(list1, list2)))  # ((1, 'a'), (2, 'b'), (3, 'c'))
dict4 = dict(zip(list1, list2))
print(dict4)  # {1: 'a', 2: 'b', 3: 'c'}

# 5通过给定“键-值对”对创建--1
dict5 = dict(key1='value1', key2='value2')
print(dict5)  # {'key1': 'value1', 'key2': 'value2'}

# 6通过给定“键-值对”对创建--2：
# fromkeys()是buildin模块里dict类的@staticmethod
list_key = [10, 11, 12]
dict6 = dict.fromkeys(list_key)  # 只有key的字典
print(dict6)  # {10: None, 11: None, 12: None}

# 7通过给定“键-值对”对创建--3
# 冒号时，key只能是tuple
list_value = ["aa", "bb", "cc"]
dict7 = {tuple(list_key): list_value}
print(dict7)  # {(10, 11, 12): ['aa', 'bb', 'cc']}

# 8字典推导式
# 略
