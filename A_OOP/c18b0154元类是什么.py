# 经典类 ，只有Python2中才有 ，继承了instance类型
class MyClass:
    pass


# 新式类 ，继承object
class Test(object):
    pass


t = Test()  # 调用了object的__new__方法去创建了t对象
print(t)  # <__main__.Test object at 0x0021F3A0>
print(type(t))  # <class '__main__.Test'> ,t是Test类创建的
print(type(Test))  # <class 'type'> ，Test类是type创建出来的
print(type(type))  # <class 'type'> ，type是type创建出来的

'''
# type，是元类： Python中所有的类都是通过type来创建出来的
# object，顶级父类： Python3中所有类的顶级父类都是object

细说：
type和object是两个独立的线，type继承自object，object是由type创建的。
类似于【先有鸡还有蛋的问题】，
不需要纠结，只要记住元类是type，顶级父类是object。
'''

'''
type源码：
# type是在buildings.py中，是个类，和str int 等类似，习惯性的称为函数，本质是个类。
# 有2个功能: 
        type(object) -> the object's type   # 一种返回对象的类型
        type(name, bases, dict) -> a new type  #  一种创建一个新类
'''
