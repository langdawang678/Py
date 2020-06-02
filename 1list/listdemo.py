# 列举部分应用，其他基本功能主要看函数和wps摘录

list1 = ['Spring', 'Summer', 11, 22]
# 1、遍历列表，换行输出列表中的每个值
for item in list1:
    print(item)

# 2、遍历列表的下标和值(用枚举函数enumerate(sequence, [start=0]))
for index, item in enumerate(list1):
    print(index, item)

# 3、直接输出列表：
print(list1)  # ['Spring', 'Summer', 11, 22]

# 4、关于枚举函数enumerate(sequence, [start=0])
'''
将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
返回 enumerate(枚举) 对象。
'''
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
enu = enumerate(seasons)
print(enu)  # <enumerate object at 0x00523B68>
print(type(enu))  # <class 'enumerate'>
print(list(enu))  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]