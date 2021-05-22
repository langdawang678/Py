"""
https://docs.python.org/zh-cn/3/reference/datamodel.html#implementing-descriptors

描述器时一个具有"绑定行为"的对象属性，该对象的属性访问通过描述其协议覆盖：__set__()和__get__()和__delete__(),如果一个对象定义了这些方法中的任意一个，它就被成为描述器

object.__get__(self,instance,owner)
获取属主类的属性（类属性访问），或者该类的一个实例的属性（实例属性访问），owner始终是主，instance是属性访问的实例，当属性通过owner访问是则为None，这个方法应该返回(计算后)的属性值，或者引发一个AttributeError异常

object.__set__(self,instance,value)
设置属主类的实例instance的属性为一个新值value

object.__delete__(self,instance)
删除属主类的实例instance的属性
"""


class Filed(object):
    # 一个类中有如下任一方法，则该类为描述器类
    def __get__(self, instance, owner):
        print("....get.....访问属性的时候被触发")
        print("__get__", self)  # <__main__.Filed object at 0x00C2F3A0>
        print("__get__", instance)  # <__main__.Model object at 0x002A8E20>
        print("__get__", owner, "\n")  # <class '__main__.Model'>
        '''class 是类,代表了调用的类名'''
        return self.value

    def __set__(self, instance, value):
        print("....set....设置属性的时候被触发")
        print("__set__:", self)  # <__main__.Filed object at 0x0029F3A0>
        print("__set__:", instance)   # <__main__.Model object at 0x00268E20>
        print("__set__:", value, "\n")  # 1000
        self.value = value
        # set不会return

    def __delete__(self, instance):
        print("...delete删除属性值的时候被触发")
        # del self.value
        self.value = None


# 描述器类,一般不直接用,他会在其他类里用
class Model(object):
    name = "aaa"
    attr = Filed()  # 是一个描述器对象: 会覆盖类属性相关操作
    '''类属性中存了个对象,对象是一个描述器类'''


m = Model()
m.name = "bbb"
print(m.name, "\n")  # bbb

m.attr = 1000
'''调用了__set__方法：
instance就是Model object,即这里的m
value就是1000
'''

# print(m.attr) # None  # __get__方法不写返回时,获取到的是None
print("获取设置后的属性值:", m.attr, "\n")  # 1000

del m.attr
print("删除后的m.attr:", m.attr)
