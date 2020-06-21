"""
BIF: enumerate()
在 for循环中，把sequence同时列出数据和数据下标。
enumerate(sequence, [start=0])
    sequence -- 一个序列、迭代器或其他支持迭代对象。
    start -- 下标起始位置。
    返回 enumerate(枚举) 对象。
"""
# enumerate() ，返回 enumerate(枚举) 对象。
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(enumerate(seasons))  # <enumerate object at 0x00593B08>
print(list(enumerate(seasons)))  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

# for 循环使用 enumerate
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)
'''
0 one
1 two
2 three
'''