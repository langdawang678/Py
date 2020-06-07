"""
zip() 映射函数
zip([iterable, ...])
    iterable -- 一个或多个迭代器;
    返回一个对象。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同

"""
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(zip(list1, list2))  # <zip object at 0x00993B28>
print(list(zip(list1, list2)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print(tuple(zip(list1, list2)))  # ((1, 'a'), (2, 'b'), (3, 'c'))
print(dict(zip(list1, list2)))  # {1: 'a', 2: 'b', 3: 'c'}
