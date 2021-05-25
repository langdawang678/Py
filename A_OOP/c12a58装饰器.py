# 1/一个最简单的装饰器
# def login(func):
#     def fun():
#         print("...登录成功...")
#         func()
#     return fun
#
#
# @login
# def getPage():
#     print("...登录后可以做其他事情")
#
#
# getPage()

# 2/带参装饰器
# def login(func):
#     def fun(a, b):
#         print("...登录成功...")
#         func(a, b)
#
#     return fun
#
#
# @login
# def getPage(a, b):
#     print("...登录后可以做其他事情" + a + b)
#
#
# getPage("a", "b")


# 3/通用装饰器
def login(func):
    def fun(*args, **kwargs):
        print("...登录成功...")
        func(*args, **kwargs)

    return fun


@login
def getPage(a, b):
    print("...登录后可以做其他事情" + a + b)


getPage("a", "b")
