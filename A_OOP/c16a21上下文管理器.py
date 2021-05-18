"""
为什么用with打开的文件,会自动关闭
"""

'''
上下文管理器是一个朋Python对象,为操作提供了额外的上下文信息.

with后面跟的是一个上下文管理器对象,
'''


class Myopen(object):
    # 文件操作的上下文管理器类
    def __init__(self, file_name, open_method, encoding="utf-8"):
        self.file_name = file_name
        self.open_method = open_method
        self.encoding = encoding

    def __enter__(self):
        self.f = open(self.file_name, self.open_method, encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
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
