"""
1.私有属性的单下划线和双下划线
  通过__dict__方法，发现双下划线会改名
2.类直接访问
3.子类可以访问父类的双下划线私有属性 （子类可继承）
"""


class Test:
    attr1 = 1000  # 类属性
    _attr2 = 2000  # 单下划线私有属性
    __attr3 = 3000  # 双下划线私有属性（为了保护数变量，会改名）

    @property
    def attr2(self):
        return self._attr2


t = Test()
print(Test.attr1)
print(Test._attr2)
# print(Test._attr3)  # AttributeError: type object 'Test' has no attribute '_attr3'


print(t.attr1)
print(t._attr2)
# print(t._attr3)  # AttributeError: 'Test' object has no attribute '_attr3'
print(Test.__dict__)
'''通过属性查看，发现变为了 _Test__attr3，此时可以通过改名后的属性名访问到
{'__module__': '__main__', 'attr1': 1000, '_attr2': 2000, '_Test__attr3': 3000, 
'__dict__': <attribute '__dict__' of 'Test' objects>, 
'__weakref__': <attribute '__weakref__' of 'Test' objects>, 
'__doc__': None}
'''


class TestB(Test):
    pass


test_b = TestB()
print(test_b.attr1)
print(test_b._attr2)
print(test_b._Test__attr3)  # 私有属性也可以被继承
