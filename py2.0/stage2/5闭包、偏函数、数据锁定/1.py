def func1(*args, **kwargs):  # 装包
    print("args:", args)
    print("kwargs:", kwargs)

    print("拆包:", *args)
    func2(**kwargs)  # **kwargs无法直接打印出来，如下
    # print("拆包:", **kwargs)  # TypeError: 'a' is an invalid keyword argument for print()


def func2(**kwargs):  # func2(a=1)再次装包 得到字典
    print("字典:", kwargs)


func1(1, 2, 3, a=1)
