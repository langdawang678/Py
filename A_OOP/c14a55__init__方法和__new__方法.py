"""
先实例化（new），在初始化（init）。
__new__ 是实例化对象的时候自动调用的
__init__ 是在创建对象的时候自动调用，对创建的对象进行初始化设置的
__new__ 方法在__init__方法之前调用，先实例了对象，在给实例初始化属性

"""

'''
作用/好处/优点：
__init__大家知道用，不做研究
__new__方法的应用场景：重写new方法可以实现单例模式
所有实例化操作都是实例一个对象，节约内存
对象属性共用，全局化
'''


class MyClass(object):
    def __init__(self, name):
        print("__init__方法调用了")
        self.name = name

    # 重写 __new__方法
    '''
    new源码里是一个类方法，@staticmethod
    '''
    def __new__(cls, *args, **kwargs):
        print("这个是new方法")
        # 创建对象是python底层帮我实现，重写之后需要返回父类的创建对象的方法，不然实例不出对象
        return object.__new__(cls)  # 调用Python内部的创建对象的方法。
        # return super().__new__(cls)  # 也可【子类调用父类方法】
        # return "123"  # 这里不会初始化，因为返回的不是MyClass类对象


m = MyClass("1111")  # 先进入new方法 在执行init方法
print(m)  # new方法里不返回的话，这里是None
print(m.name)
