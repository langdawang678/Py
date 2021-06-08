"""
1/自定义元类的创建
2/子类使用
3/孙子类继承
4/类的创建过程: 找metaclass指定的类,找不到则用内置的type去创建类
5/应用:将类的所有属性名改为大写 (创建类的时候,不想被看到区别,可以在底层修改,即在元类这里修改)

6/补充:
字典.items() 返回的是一个生成器对象,为了省内存
"""


# 自定义元类必须继承于type
class MyMetaClass(type):
    """自定义的元类"""
    def __new__(cls, name, bases, attr_dict, *args, **kwargs):
        print("最基础的自定义元类")

        # 遍历属性名
        for k, v in attr_dict.items():
            attr_dict.pop(k)
            attr_dict[k.upper()] = v

        # attr_dict["__slots__"] = ['name', 'age', "gender"]
        '''限制对象创建__dict__属性,即当 m = MyTest(), print(m.__dict__)时,找不到这个属性的'''
        # return type.__new__(name, bases, attr_dict)  # 用type调用new方法不需要cls
        return super().__new__(cls, name, bases, attr_dict)
print(MyMetaClass.__bases__)  # (<class 'type'>,)


# 通过自定义元类去创建类
class MyTest(metaclass=MyMetaClass):  # 指定元类, 不是继承这个MyMetaClass
    name = 'qqq'
print(type(MyTest))  # <class '__main__.MyMetaClass'>


# print(MyTest.name)  # qqq
print(MyTest.NAME)  # qqq
print(MyTest.__dict__)  # 如下
'''
{'__MODULE__': '__main__', '__QUALNAME__': 'MyTest', 'NAME': 'qqq',
 '__module__': '__main__', '__dict__': <attribute '__dict__' of 'MyTest' objects>,
  '__weakref__': <attribute '__weakref__' of 'MyTest' objects>, '__doc__': None}
'''
'''
1/下面的小写的是在new方法时调用的,没有在改大写时调用
2/__module__被改成大写了,没有检测到,所以下面又生成了一个'''


# 对比非继承自定元类的
class Test1(object):
    pass
print(type(Test1))  # <class 'type'>



# # 自定义元类可以继承给孙子
# class MyTest2(MyTest):
#     pass
# print(type(MyTest2))  # <class '__main__.MyMetaClass'>
# '''这个仅演示继承, 在改大写时会报错: RuntimeError: dictionary keys changed during iteration'''