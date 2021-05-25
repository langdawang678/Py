# 2/带参装饰器
def extend(func):
    def fun(a, b):
        print(a // b)
        print(a % b)
        func(a, b)

    return fun


@extend
def add_num(a, b):
    print("加法{}+{}=".format(a, b), a + b)
    print(f"加法{a}+{b}={a+b}")


add_num(10, 3)
