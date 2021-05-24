"""
1.什么是闭包:函数外部调用了函数内部定义的函数。

2.条件
条件1:函数中嵌套函数
条件2:外层函数返回内层嵌套函数名
条件3:内层嵌套函数,有引用外层函数的一个非全局变量

3.作用
数据锁定,提高数据的安全性.
(c12a45开始)

4.装饰器就是必要的一个应用
"""

a = 100  # 全局变量 ,不会放在res的__closure__中.因为本身在任何地方都可被访问,放进去也没有意义.


# 这个login是全局变量里的,下面的func可以调用
def login():
    print(".....调用了函数login")


def func(num, num2):
    login()
    print("a =", a)
    # num = 100 # func无参数,直接在func内部定义num,也是条件3中的"外层函数的一个非全局变量"
    print("....调用了函数func")

    def count_book():  # 闭包条件1
        print("闭包条件3:", num, num2, a)  # 闭包条件3
        '''这里a仅做__closure__的演示,实际不应该有a在这里被引用'''
        print("...调用了函数count_book")

    return count_book  # 闭包条件2:外层函数,返回内层函数的函数名
    '''不return的话,不能访问内层的函数'''


# func()  # func函数里的 函数,不能直接调用,因为是在[局部变量]里的.
res = func(100, [22, 33])
res()  # ...调用了函数count_book
'''func()()等效于res()'''

print(res)  # <function func.<locals>.count_book at 0x7fc349289a70>
print(res.__closure__)
'''返回
(<cell at 0x7fa7d2783d10: int object at 0x1068b2780>, <cell at 0x7fa7d3897c50: list object at 0x7fa7d25931e0>)
# 返回了元组,里面是 一个int object ,一个是 list object

把闭包函数引用的一个非全局变量,存在__closure__这个属性中,用到的时候去这个属性里拿. 
--> 锁定数据,调高数据的安全性.
防止外部的变量改变了,导致内部函数的结果变化.
'''
print()
