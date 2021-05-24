class MyClass(object):
    __instance = None

    # 重写 __new__方法
    def __new__(cls, *args, **kwargs):
        # 如果 instance 为None 实例化对象,否则用第一次实例的对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            # MyClass.__instance = object.__new__(cls)  # 也可，类属性通过类名调用
            return cls.__instance
        else:
            return cls.__instance


m1 = MyClass()
m2 = MyClass()
# id 一样 同一个对象
print(id(m1))  # id相同的
print(id(m2))  # id相同的

# 所以m1创建的属性，m2一样有
m1.name = "111"
print(m2.name)
