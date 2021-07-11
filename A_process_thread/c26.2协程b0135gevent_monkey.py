"""
gevent切换还是要主动用自己的等待标志(gevent.sleep)才会切换，还不够强大
gevent有一个补丁可以智能的切换，在IO阻塞的时候(有耗时)自动切换
导入补丁：from gevent import monkey
线程中调用：monkey.patch_all()
此时只要有耗时操作就会自动切换
注意： 一个进程内调用一次monkey.patch_all()方法即可
多进程内每个子进程内调用，不能在主进程中调用
多线程主线程内调用，不能每个子线程都调用
"""

from gevent import monkey
# 放在导包之前，会改系统的环境
# 不然会有警告
monkey.patch_all()
import time
import requests
import gevent


def work1(a):
    for i in range(10):
        res = requests.get("http://www.baidu.com").status_code
        print("---work{}----{}的结果：{}".format(a, i, res))


def work2(a):
    for i in range(10):
        res = requests.get("http://www.baidu.com").status_code
        print("---work{}----{}的结果：{}".format(a, i, res))


# 创建两个gevent对象
# 参数*args, **kwargs
# 默认就已经开启执行了
st = time.time()
g1 = gevent.spawn(work1, a=1)
g2 = gevent.spawn(work2, a=2)

# 线程等待协程执行完
g1.join()
g2.join()
# work1(1)
# work2(2)
et = time.time()
print("时间：", et - st)

# 两个协程：时间： 0.4506347179412842
# 单线程 ： 时间： 0.7228543758392334
