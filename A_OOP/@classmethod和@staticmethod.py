
"""写的比较好的文章:https://www.cnblogs.com/wcwnina/p/8644892.html"""
'''
1.实例方法只有实例调用,就是self
2.类方法,可以类去调用,cls
3.静态方法,在类里,但不接受类和实例的参数/方法,逻辑性代码可以类和实例调用,无self和cls


静态方法是类中的函数，不需要实例。
静态方法主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，不会涉及到类中的属性和方法的操作。
可以理解为，静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于使用和维护。
'''

"""
总结:
                    实例的属性和方法    类的属性和方法     参数        可被谁调用
实例方法:                   可访问        可访问          self        仅实例调用
@classmethod的方法:         不可访问      可访问          cls         类和实例
@staticmethod的方法:        不可访问      不可访问        空           类和实例
"""

def func():
    print("普通方法,python直接调用")


class Test:
    num = 100  # 类属性

    def __init__(self, age):
        self.age = age  # 实例属性

    def func(self):  # 第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）
        self.num += 1
        s = self.age
        print("实例方法,要加self")

    @classmethod
    def classfunc(cls):  # 第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）
        cls.num += 1
        # s = cls.age  # AttributeError: type object 'Test' has no attribute 'age'
        '''（不能传实例的属性和方法）'''
        print("classmethod,类方法要加cls.方便类直接调用")

    @staticmethod
    def staticfunc():  # 参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法
        print("staticmethod,静态方法,不要self和cls. 因为它和类功能相关,但是又和类的属性&实例没关系")

func()  # 普通方法,python直接调用

t = Test("111")
t.func()  # 实例方法,要加self

t.classfunc()  # classmethod,类方法要加cls.方便类直接调用
Test.classfunc()  # classmethod,类方法要加cls.方便类直接调用

Test.staticfunc()  # staticmethod,静态方法,不要self和cls. 因为它和类功能相关,但是又和类的属性&实例没关系
t.staticfunc()  # staticmethod,静态方法,不要self和cls. 因为它和类功能相关,但是又和类的属性&实例没关系
