"""
鸭子类型: [强数据类型,多态,伪多态]

1:
Python中参数是没有类型限制的,多态在Python的的体现不是很严谨.
多态的概念应用于Java/C这种类强类型语言中 (子类重写父类方法),Python崇尚的是"鸭子类型"

2:
鸭子类型:一个对象,只要看起来像鸭子,走起来像鸭子,那么它就是个鸭子.
Python解释器不检查发生多态的对象,是否继承了同一个父类,只要它们有相同的行为(方法),它们之间就是多态的.
(不要求严格的继承体系,关注的不是对象的类型本身,而是它如何使用的.)

"""


def start(obj):
    # python函数中的参数是没有类型限制的
    # 此处的参数是一个对象. 函数里的对象调用了方法.
    obj.speak()


# 伪多态的实现
class Animal:
    def speak(self):
        print("动物叫,但不知道是哪种动物在叫")


class Dog(Animal):
    def speak(self):
        print("Dog speak")


class Cat(Animal):
    def speak(self):
        print("Cat speak")


class Car:
    def speak(self):
        print("Car speak")


start(Animal())
start(Dog())

cat_obj = Cat()
print(isinstance(cat_obj, Animal))  # True 子类的对象,也属于父类
start(cat_obj)

start(Car())

'''
动物叫,但不知道是哪种动物在叫
Dog speak
True
Cat speak
Car speak
'''
