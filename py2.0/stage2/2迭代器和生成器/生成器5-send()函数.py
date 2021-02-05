"""
了解下就行了，不管太细节。
1. send()和__next__()都是让生成器向下走一次。
2. send()可以给上一个yield的位置传递，不能给最后一个yield发送信息，在第一次执行生成代码时候不能用send()。
"""

def eat():
    print("start...")
    a = yield "aaaaa"

    print("a =", a)
    b = yield "bbbbb"

    print("b =", b)
    c = yield "cccc"

    print("c =", c)
    yield "GAME OVER"


g = eat()
print(g.__next__())  # 第一次执行时候不能使用send() ，因为是给上一个yield赋值
# start...
# aaaaa
print(g.__next__())
# a = None
# bbbbb
print(g.send("第一次send"))
# b = 第二次send
# cccc
print(g.__next__())  # 运行结束后，yield返回None
# c = None
# GAME OVER

'''
start...
aaaaa
a = None
bbbbb
b = 第一次send
cccc
c = None
GAME OVER
'''

'''分析：https://blog.csdn.net/qq_33567641/article/details/81097709
g = eat()获取函数生成器，调用__next__()时，函数打印我吃什么，然后打印馒头，
此时理论上不给a赋值的话，将返回None，但是我们可以使用send()通过生成器对a赋值，
使之获得“饺子”字符串，所以打印a = “饺子”，程序往下执行亦是如此。'''
