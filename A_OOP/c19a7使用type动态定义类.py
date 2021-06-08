"""
使用元类type,完成模拟类和方法的创建和调用
(实际中不会这么去用,这里是为了了解底层原理)
"""


# 类是元类的实例对象 (19-1828)
# 空元组(), 元组中只要一个元素(obj,)

# 使用元类type,完成模拟类和方法的创建和调用
def func(self):
    print('-----这个是self-----')
Test = type('Test', (object,), {"attr": 100, "__attr2": 200, "function01": func})
'''
参数说明:
type(name, bases, dict) -> a new type  #  一种创建一个新类
    参数1/类名 -str ,即类的__name__属性
    参数2/继承的父类 -tuple ,可不传,即类的__base__属性
    参数3/方法和属性 -dict,即类的__dict__属性
'''
print(Test)  # <class '__main__.Test'>
print(Test.__bases__)  # (<class 'object'>,)
'''# Python 为所有类都提供了一个 bases 属性，
通过该属性可以查看该类的所有直接父类，该属性返回所有直接父类组成的元组。
注意是直接父类！！！
'''

# 元类的方法调用
t = Test()
t.function01()  # -----这个是self-----


# 用type元类创建类,等效于下面这个
class Test1:
    attr = 100
    __attr2 = 200

print(Test1)  # <class '__main__.Test1'>

'''
Test = type('Test111', (object,), {"attr": 100, "__attr2": 200, "function01": func})
print(Test)  # <class '__main__.Test111'>
    Test111 是真正的类名
    Test 是对类名的引用
'''