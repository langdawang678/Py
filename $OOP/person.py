"""
演示类和对象的类型
"""

class Person:
    pass


# 类,class
print(Person)  # <class '__main__.Person'>

# 对象,object（无入参）
print(Person())  # <__main__.Person object at 0x0032FFB8>
man = Person()
print(man)  # <__main__.Person object at 0x0050FF88>
