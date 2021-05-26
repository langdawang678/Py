"""
https://blog.csdn.net/pythondafahao/article/details/79533480

python的四个作用域LEGB:
局部作用域(函数内)  Local(Function)      L
外部嵌套函数作用域  Enclosing Function locals E  nonlocal
函数定义所在模块的作用域 Global(module)      G
python内置模块的作用域 Builtin(Python)     B

变量名的查找规则: 在访问变量时，先查找本地变量(局部变量), 然后是包裹此函数外部的函数内部的变量，之后是全局变量，最后是内置变量
L  ->  E  -> G  -> B

"""

var = 100


def outter():
    var = 200
    print("outer:", var)

    def inner():
        nonlocal var
        var += 1
        print("inner:", var)

    inner()
    print("outer被改变了,,,", var)


outter()
print("全局的", var)
'''输出结果
outer: 200
inner: 201
outer被改变了,,, 201
全局的 100
'''
'''nonlocal说明:
 1. nonlocal 语句只能在被嵌套函数内部进行使用
 2. 访问nonlocal变量将对外部嵌套函数作用域内的变量进行操作
 3. 当有两层或两层以上函数嵌套时，访问nonlocal变量只对最近的一层变量进行操作
 4. nonlocal语句的变量列表里的变量名不能出现在此函数的参数列表里
'''