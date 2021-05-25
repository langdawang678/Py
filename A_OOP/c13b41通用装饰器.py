

# 3/通用装饰器(有没有参数都可以)
def add(func):
    def fun(*args, **kwargs):
        print("...登录成功...")
        func(*args, **kwargs)

    return fun


@add
def index():
    print("...欢迎进入首页")


@add
def goods_list(num):
    print(f"这个是第{num}页的商品")


index()
print("- - - - - - - - -")
goods_list(2)
