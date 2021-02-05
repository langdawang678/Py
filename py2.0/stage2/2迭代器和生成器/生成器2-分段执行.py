# return是直接结束函数的执行，yield是分段来执行函数。
def func():
    print("111")
    yield 222
    print("333")
    yield 444
gener = func()
ret = gener.__next__()
print(ret)  # 222
ret2 = gener.__next__()
print(ret2)  # 444
