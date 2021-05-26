"""编写装饰器，
为多个函数加上认证的功能（用户的账号密码来源文件），
要求登录一次成功，后续的函数都无需再次输入用户名和密码，
"""
import json

with open("c14a11userinfo.txt") as f:
    info_str = f.read()
    print(type(info_str))  # <class 'str'>

    # info_dict = json.loads(info_str)
    # print(type(info_dict))  # <class 'dict'>
    info_dict = eval(info_str)
    print(type(info_dict))
'''token存在用户的cookies中,如果用户的cookies'''

def login(func):
    print("1//进入login")

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