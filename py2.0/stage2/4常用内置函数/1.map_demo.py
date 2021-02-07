"""
一句话：map是序列在函数上做隐射
描述
  map() 会根据提供的函数对指定序列做映射。
  第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
语法：
  map(function, iterable, ...)
参数：
  function -- 函数的名称（不带括号）
  iterable -- 一个或多个序列
返回值：
  Python 2.x 返回列表。
  Python 3.x 返回迭代器。
"""


# demo1
def demo1(x):
    return x * 2
list1 = [1, 2, 3]
res = map(demo1, list1)  # 直接函数名，不需要括号。
print(res)  # <map object at 0x7fbbe2a83d10>
print(list(res))  # [2, 4, 6]

# demo2
def demo2(x):
    return x ** 2
map(demo2, [1, 2, 3, 4, 5])  # [1, 4, 9, 16, 25]

# demo3,使用表达式：使用 lambda 匿名函数
map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # [1, 4, 9, 16, 25]

# demo4，提供了两个列表，对相同位置的列表数据进行相加
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])  # [3, 7, 11, 15, 19]
