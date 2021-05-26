def func1(*args, **kwargs):  # 装包
    print("*args:", args)  # (1, 2, 3)
    print("**kwargs:", kwargs)  # {'a': 1}

    print("拆包:", *args)  # 1 2 3
    print("拆包:", args)  # (1, 2, 3)
    # print("拆包:", **kwargs)  # TypeError: 'a' is an invalid keyword argument for print()
    print("拆包:", *kwargs)  # a
    print("拆包:", kwargs)  # {'a': 1}


print("------------------")


def func2(**kwargs):  # func2(a=1)再次装包 得到字典
    print("字典:", kwargs)  # {'a': 1}


func1(1, 2, 3, a=1)

print("------------------")


def func3(*args):
    print(args)


tu = (1, 2, 3, 4)
func3(tu)  # ((1, 2, 3, 4),)
func3(*tu)  # (1, 2, 3, 4) 拆包了
