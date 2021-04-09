"""
reversed 函数返回一个反转的迭代器。
reversed(seq)
    seq -- 要转换的序列，可以是 tuple, string, list 或 range。
    返回一个反转的迭代器。
"""

# 字符串
seqString = 'Runoob'
print(list(reversed(seqString)))

# 元组
seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
print(list(reversed(seqTuple)))

# range
seqRange = range(5, 9)
print(list(reversed(seqRange)))

# 列表
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))