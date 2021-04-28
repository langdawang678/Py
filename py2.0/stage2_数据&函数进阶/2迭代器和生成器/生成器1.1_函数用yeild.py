"""普通函数的return变为yield，那么这个函数就是一个生成器
return是直接结束函数的执行，yield是分段来执行函数
yeild只能在函数中用"""

def gen(a):
    n = 0
    while n < a:
        n += 1
        yield n  # yield的作用和return一样. 也是返回数据。
g = gen(2)  # 这个时候函数不会执行，而是获取到生成器
print(g)  # <generator object gen at 0x7f8342885150>
'''
生成器的本质就是迭代器，
我们可以通过执行__next__()来执行获取结果
'''
print(g.__next__())  # 1
print(g.__next__())  # 2
print(g.__next__())  # 报错：StopIteration


