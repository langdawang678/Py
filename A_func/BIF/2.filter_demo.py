"""
描述：
  filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象。
  如果要转换为列表，可以使用 list() 来转换。
  该接收两个参数，第一个为函数，第二个为序列。
  序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
语法：
  filter(function, iterable)
参数：
  function -- 判断函数。
  iterable -- 可迭代对象。
返回值：
  返回一个迭代器对象

"""

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def demo_1(x):
    if x % 2 == 0:
        return x
print(filter(demo_1, list_1))  # <filter object at 0x7f80229d1450>
print(list(filter(demo_1, list_1)))

