# 4/装饰器装饰类的时候,必须加return
def add(func):
    def fun(*args, **kwargs):
        print("...登录成功...")
        return func(*args, **kwargs)  # <__main__.MyClass object at 0x7f94dbf8fbd0>
        '''本来是 直接执行func(xxx),现在是多了return'''
    return fun


@add  # MyClass = add(MyClass)
class MyClass:
    def __init__(self, name, age):
        print("...init")
        print(name, age)


m = MyClass("111", 18)
'''因为add是通用装饰器,所以MyClass在调用的时候,传不传参都可以'''
print(m)  # None  装饰器不返回时,类的对象就是None
