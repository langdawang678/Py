"""
__slots__属性：
1.限制对象所能绑定的属性
（也可以防止实例在调用的时候手误）
2.节约内存：定义了slots后，该对象不会再自动生成__dict__属性
（在知道需要用那些属性的前提下，可以用这个进行内存优化）
"""


class Base(object):
    __slots__ = ["name"]  # 子类无法继承这个属性（试一下就知道了）

    # def __init__(self, name, age):
    def __init__(self, name):
        self.name = name
        # self.age = age


# t = Test("cxh", 18)  # AttributeError: 'Base' object has no attribute 'age'
t = Base("111")

# 有__slots__时，加其他属性会报错
# t.age = 200  # AttributeError: 'Test' object has no attribute 'age'
# print(t.__dict__)  # AttributeError: 'Test' object has no attribute '__dict__'
