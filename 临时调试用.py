"""类装饰器:
通过类实现一个通用的装饰器
即可装饰类,也可装饰函数
"""


class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("...装饰器里的功能1")
        # self.func(*args, **kwargs)
        return self.func(*args, **kwargs)
        # print("...装饰器里的功能2")


# 1/装饰函数
@Decorator  # test01 = Decorator(test01)
def test01(a):
    print("fun1原来的函数", a)


'''核心思路:
@Decorator  # test01 = Decorator(test01) 
上面的的Decorator(test01) 相当于实例化了一个对象.
那调用test01()行数的时候,相当于对象直接加括号调用,所以类中要实现call方法

'''


# 2/装饰类
@Decorator
class My:
    def __init__(self, name):
        self.name = name
        print("类原来的功能")


if __name__ == '__main__':
    print(test01)  # <__main__.Decorator object at 0x0027F3A0>, 是 Decorator的实例化对象,同上面的思路
    test01(1111)
    print("-----------------")
    print(My)  # <__main__.Decorator object at 0x0260E028> ,同上
    m = My("111")
    print(m)   # <__main__.My object at 0x011DE1F0>,需要在Decorator中call方法加return原函数
