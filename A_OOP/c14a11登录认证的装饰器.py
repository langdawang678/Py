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
    def fun(*args, **kwargs):
        if info_dict["token"] == "False":
            user_in = input("请输入账号:")
            pwd_in = input("请输入密码:")
            if info_dict["user"] == user_in and info_dict["pwd"] == pwd_in:
                info_dict["token"] = "True"
                with open("c14a11userinfo.txt", "w") as f:
                    f.write(str(info_dict))
                print("...登录成功...")
            else:
                print("...登录失败...")
        else:
            print("已经登录了,不需要再登录")
        func(*args, **kwargs)

    return fun


@login
def index():
    print("...网站首页...")


print("------------")


@login
def goods():
    print("...商品页...")


index()
goods()
