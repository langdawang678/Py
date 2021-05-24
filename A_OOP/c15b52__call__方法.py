"""
问题一：在Python中万物皆对象，函数也是对象，为什么函数可以调用，而其他的对象不行呢？
如果想让类创建出来的对象，可以像函数一样被调用可以实现么？
那么我们只需要在类中定义__call__方法即可
"""


# __call__ 可以被调用的方法 像函数一样加() 可以被调用，
# 实例不能被调用是因为 实例和函数底层实现的方法不一样
# 函数底层实现的call方法
def fun():
    print("函数")


class My(object):
    def __init__(self, name):
        print("这个是init方法")
        self.name = name


print("函数内部实现的方法", dir(fun))  # 实现了'__call__'
m1 = My("DaBai")
print("实例实现的方法", dir(m1))  # 没有实现__call
m1()  # 被执行会报错


class My(object):
    def __call__(self, *args, **kwargs):
        print("__实例被执行了__")


m = My()
m()  # 不会报错 会执行类中__call__方法内的代码块
