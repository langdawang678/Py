# 不建议用进程继承的方式,创建比较麻烦,一般用进程池
# 进程池里的进程,都有各自的资源.

"""

当需要创建的子进程数量过多的时候，我们可以利用进程池来创建

初始化Pool的时候，可以指定一个最大进程数，当前新的请求提交到Pool中中时，
如果池中还没有满，那么就会创建一个新的进程用来执行该请求，
但是如果池中的进程数已经达到最大值，那么该请求就会等待，直到池中有进程结束，才会用之前的进程来执行新的任务

Pool常用的方法
    apply_async(func,args=(),kwds={},callback=None,error_callback=None)： 使用非阻塞的方式调用func(并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程)
    close() : 关闭进程池
    terminate()：不管子进程是否结束，立即终止
    join() ：主进程阻塞，等待子进程结束，必须在close或terminate之后使用
"""
from multiprocessing import Pool, Manager
import os
import time

a = 0


def work(q):
    print(f"任务执行{a}", os.getpid())
    time.sleep(0.5)  # 不加的话一个进程全部执行完了


if __name__ == '__main__':
    q = Manager().Queue()  # 进程池之间的队列
    for i in range(10):
        q.put("127.0.0.1")

    pool = Pool(3)  # 创建进程池,3个进程
    # 创建10个任务
    for i in range(10):
        if q.qsize() > 0:
            pool.apply_async(work, args=(q,))
        else:
            break
    pool.close()
    pool.join()
'''
线程池,用的第三方库 (自行扩展)
Python的并发中用的最多的是协程(效率最高),然后进程(进程太占用资源了),然后线程(线程用在网络/IO上)
'''
