"""用装饰器实现单例模式
可用于多个类"""


def single(cls):
    __instance = {}  # 空字典储存 类 和 类实例（key:value）

    def inner(*args, **kwargs):
        # 如果类不在字典中实例化对象储存，否者用字典中的对象
        if cls in __instance:
            print(__instance)
            return __instance[cls]
        else:
            __instance[cls] = cls(*args, **kwargs)
            return __instance[cls]
    return inner


@single
class Test:
    def __init__(self, name):
        self.name = name
        print("...Test类初始化", self.name)

@single
class Hello:
    def __init__(self, name):
        self.name = name
        print("...Hello类初始化", self.name)


t1 = Test("111")
t2 = Test("222")
print(t1.name)
print(t2.name)
print("------------------------------------------------")
h1 = Hello("hhh")
h2 = Hello("xxxxxxxxx")
print(h1)
print(h2)