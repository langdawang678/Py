# --- 1.无参,无返回--- #
def func1(func):
    def func2():  # 内函数中，完成对额外功能的添加，调用原来的函数
        print("无参，无返回值")
        func()

    return func2


@func1
def t1():
    print("test")


t1()


# --- 2.无参,有返回--- #
def func1(func):
    def func2():
        print("无参，有返回值")
        return func()  # return返回函数的返回值

    return func2


@func1
def t2():
    return 1


print(t2())


# --- 3.有参,无返回--- #
def func1(func):
    def func2(args):
        print("有参，无返回")
        func(args)  # 返回用户传的参数

    return func2


@func1
def t3(args):
    print(args)


t3(123)


# --- 4.有参,有返回--- #
def func1(func):
    def func2(args):
        print("有参，有返回")
        return func(args)

    return func2


@func1
def t4(args):
    return args


print(t4(45))
