"""
把字符串脱衣服
"""

x = 7
eval('3 * x')  # 21
eval('pow(2,2)')  # 4
eval('2 + 2')  # 4
n = 81
eval("n + 4")  # 85

def demo1():
    print("eval 表达式的作用")

eval("demo1()")  # 这里等效于调用demo1()函数，打印了：eval 表达式的作用
