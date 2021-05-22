
"""
官方文档：
https://docs.python.org/zh-cn/3/reference/datamodel.html#customizing-attribute-access

内置的魔术方法，在增删查时会触发，重写则可以完成特定的赋值/逻辑，
但还是要调用父类的，因为重写的只是加了逻辑，并没有增删查的实现。
(调用父类的有 object和super()两种方式,注意入参有没有 self)
"""


class Test:
    def __init__(self):
        self.age = 18

    # 官方文档提示：当找不到属性的时候要么抛出异常
    # 要么返回一个特定的数值
    def __getattr__(self, item):
        # 当我们访问属性的时候，属性不存在的时候触发该方法,出现AttrError
        print("----这个是__getattr__方法----")
        # return super().__getattribute__(item)
        # return object.__getattribute__(self, item)
        '''super()相当于是个实例，不用加self'''
        '''object类，需要加self'''
        return 100

    def __getattribute__(self, item):
        # 访问/查找属性的时候第一时间触发
        print("----__getattribute__----")
        # 返回父类查看属性的功能方法
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        # 设置属性时，调用该方法设置属性
        # print("__setattr__=", key)  # 属性名称
        # print("__setattr__=", value)  # 属性值
        # 可以重写这个设置一些干扰操作
        if key == "age":
            # 这样属性在外界对age的修改不会生效
            return super().__setattr__(key, 18)
        # 返回父类的设置属性的方法
        return super().__setattr__(key, value)

    def __delattr__(self, item):
        # 在del obj.attr删除属性时触发
        print("__delete__被触发了")
        # 我们可以控制哪个属性不能被外界删除
        print(item)
        if item == "age":
            print("不能被删除")
        else:
            return super().__delattr__(item)


t = Test()
# 设置属性的时候 触发__setattr__
t.name = "DaBai"
# 先触发查找的方法，找到了不会在去触发__getattr__方法
print(t.name)
# 先触发查找方法，找不到才去触发__getattr__方法
print(t.name1)

# 设置修改age属性，触发__setattr__
t.age = 1111111
t.name = "2222222"
print(t.age)  # >>>在 __setattr__方法中过滤了，还是18
print(t.name)  # 会被修改

# 删除的时候触发__delattr__
del t.name
print(t.name)  # 属性删除了
del t.age
print(t.age)  # 过滤了这个属性不能在被外界删除了
