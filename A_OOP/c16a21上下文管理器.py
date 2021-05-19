"""
为什么用with打开的文件,会自动关闭
"""

'''
上下文管理器是一个Python对象,为操作提供了额外的上下文信息.
如果一个类中有__enter__ , __exit__方法,那么这个类就可以当做一个上下文管理器用.

with后面跟的是一个上下文管理器对象,
with将enter的返回值,绑定到as后面的对象上.

上下文管理器可以由with语句开启，
当程序进入with语句块时，就运行 __enter__()魔术方法并把所返回的对象, 赋值给as后的对象,可以在上下文中使用。
当执行语句流要离开with语句块时，调用上下文管理器的(前面返回对象的) __exit__()方法将清理所使用的全部资源。
'''


class Myopen(object):
    # 文件操作的上下文管理器类
    def __init__(self, file_name, open_method, encoding="utf-8"):
        self.file_name = file_name
        self.open_method = open_method
        self.encoding = encoding
        # #也可以这里open文件,enter里直接返回.

    def __enter__(self):
        # 启动上下文,返回文件对象
        self.f = open(self.file_name, self.open_method, encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 退出上下文时,将文件关闭
        # 类型;值;源头(traceback)
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        self.f.close()


with Myopen("c16a21_Context Manager.txt", "r") as f:
    print(f)  # <_io.TextIOWrapper name='c16a21_Context Manager.txt' mode='r' encoding='utf-8'>
    '''上面是一个文件操作句柄,默认编码是cp936,即GBK,因为是code page的936页'''
    print(name)  # <class 'NameError'>  # <traceback object at 0x7faa3c794910>
    print(f.read())
