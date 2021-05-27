"""
# todo

1、https://www.cnblogs.com/jiangmingbai/p/10909449.html#%E6%96%B9%E5%BC%8F%E4%BA%8C%EF%BC%9A%E5%8D%95%E4%BE%8B%E8%A3%85%E9%A5%B0%E5%99%A8
2、16的开头
"""


# 装饰器单例模式
def class_one_case(cls):
    # 空字典储存 类 和 类实例（key:value）
    __instance = {}

    def inner(*args, **kwargs):
        # 如果类不在字典中实例化对象储存，否者用字典中的对象
        if cls not in __instance:
            __instance[cls] = cls(*args, **kwargs)
            return __instance[cls]
        else:
            return __instance[cls]

    return inner


@class_one_case
class TestClass(object):  # TestClass=class_one_case(TestClass) 调用的时候执行的装饰器内部inner方法，返回实例
    name = "111"

    def run(self):
        print(self.name)


t1 = TestClass()
t2 = TestClass()
print(id(t1))
print(id(t2))
t1.name = "222"
# t2 就是t1  name 属性也都公共也变成"222"
t2.run()  # 222 # 注释掉装饰器,则这里打印111
