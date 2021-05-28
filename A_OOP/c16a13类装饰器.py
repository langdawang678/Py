# 类装饰器
class MyCall(object):
    def __init__(self, fun_cls):
        # print("这个是init方法")
        self.fun_cls = fun_cls

    def __call__(self, *args, **kwargs):
        print("call方法")
        return self.fun_cls(*args, **kwargs)


@MyCall
def fun(a):  # fun = Mycall(fun)  此时的fun 是 Mycall的实例对象了,被调用时执行call方法
    print("函数%s" % a)


@MyCall
class My(object):  # My = Mycall(My)  此时的My 是 Mycall的实例对象了,被调用时执行call方法
    def __init__(self, name):
        self.name = name


print(fun)  # <__main__.MyCall object at 0x0000022ECE480320> MyCall的实例对象
fun(1)  # 实例被执行 执行的call方法，call方法里面执行了run()函数

print(My)  # <__main__.MyCall object at 0x0000012B8FDB03C8> MyCall的实例对象
m = My("111")  # MyCall的实例对象执行call方法 返回 My类的实例对象
print(m)  # <__main__.My object at 0x0000012B8FDB0470> My的实例对象
