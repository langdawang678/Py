"""
一句话：zip是序列和序列之间做映射
描述:
  zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
  然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
  如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同.
语法：
  zip([iterable, ...])
参数说明：
  iterabl -- 一个或多个迭代器;
返回值：
  返回一个对象
"""
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(zip(list1, list2))  # <zip object at 0x00993B28>
print(list(zip(list1, list2)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print(tuple(zip(list1, list2)))  # ((1, 'a'), (2, 'b'), (3, 'c'))
print(dict(zip(list1, list2)))  # {1: 'a', 2: 'b', 3: 'c'}

# 解压
a = [1, 2, 3]
b = [4, 5, 6]
# a1, a2 = zip(*zip(a, b))  # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
zipped = zip(list1, list2)
a1, a2 = zip(*zipped)  # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
print(list(a1))
print(list(a2))
