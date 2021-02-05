# 生成器可以使用for循环来获取内部元素：
def func():
    print(111)
    yield 222
    print(333)
    yield 444
    print(555)
    yield 666
gen = func()
for i in gen:
    print(i)