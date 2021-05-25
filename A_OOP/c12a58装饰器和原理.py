"""
1)解释/原理：
装饰函数是一个闭包样式的函数，入参是[被装饰函数],返回是[内部函数名].
(即被装饰函数的函数名, 是装饰器函数的入参.)
被装饰器的函数名指向了装饰器内部函数
内部函数中加了新功能,并调用了原函数(被装饰的函数)

目的：遵循原则，开放扩展 关闭修改

2)好处/作用:
在不改变原函数功能的情况扩展功能
执行原函数就能执行到扩展功能

3)装饰器的应用场景:
登录验证
函数运行时间统计
执行函数之前做准备工作
执行函数后做清理功能, 数据库断开之类的
"""


# 1/一个最简单的装饰器
def login(func):
    print("1//进入login")

    user = "1"
    pwd = "1"

    def fun():
        print("3//进入fun")
        user_in = input("请输入账号:")
        pwd_in = input("请输入账号:")
        if user == user_in and pwd == pwd_in:
            print("...登录成功...")
            print("4//执行被装饰的函数func")
            func()
        else:
            print("...登录失败...")
    print("2//返回fun")
    return fun


@login
def index():
    print("5//执行被装饰的函数func指向的index()函数")
    print("...网站首页...")


'''
@login是语法糖,在index()调用时,其实是 index = login(index),
把index函数名作为入参,传到login函数中
'''

index()
'''
去掉@login再注释掉index()后,效果同下:
index111 = login(index)
index111()
'''

"""
# index 传到(指向)fun
# index是函数login的局部变量fun
print(index)  # <function login.<locals>.fun at 0x006426A0>

# index存储在了closure属性中
print(index.__closure__)
# (<cell at 0x0047F3A0: function object at 0x006426E8>, <cell at 0x0047FA90: str object at 0x0045E4E0>, <cell at 0x00632EF8: str object at 0x0045E4E0>)
'''1个function object,2个str'''
"""