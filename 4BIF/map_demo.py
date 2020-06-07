"""
map() 会根据提供的函数对指定序列做映射。
map(function, iterable, ...)
    function -- 函数
    iterable -- 一个或多个序列
    Python 3.x 返回迭代器。

"""
def square(x):  # 计算平方数
    return x ** 2
# 计算列表各个元素的平方
map(square, [1, 2, 3, 4, 5])  # [1, 4, 9, 16, 25]

# 使用 lambda 匿名函数
map(lambda x: x ** 2, [1, 2, 3, 4, 5])
# [1, 4, 9, 16, 25]

# 提供了两个列表，对相同位置的列表数据进行相加
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
# [3, 7, 11, 15, 19]
