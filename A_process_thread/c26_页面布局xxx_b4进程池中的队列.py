
# 不建议用进程继承的方式,创建比较麻烦,一般用进程池
# 进程池里的进程,都有各自的资源.


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
            pool.apply_async(work,args=(q,))
        else:
            break
    pool.close()
    pool.join()
'''
线程池,用的第三方库 (自行扩展)
Python的并发中用的最多的是协程(效率最高),然后进程(进程太占用资源了),然后线程(线程用在网络/IO上)
'''
