
# 不建议用进程继承的方式,创建比较麻烦,一般用进程池
# 进程池里的进程,都有各自的资源.

# 接[c26_页面布局xxxx]
from multiprocessing import pool
import os
import time

a = 0


def work():
    print(f"任务执行{a}", os.getpid())

    time.sleep(0.5)  # 不加的话一个进程全部执行完了


if __name__ == '__main__':
    p = pool.Pool(3)  # 创建进程池,3个进程

    # 创建10个任务
    for i in range(10):
        p.apply_async(work)

    p.close()  # 关闭进程池
    p.join()  # 主进程等待进程池中的所有进程都执行结束后,再往下执行.

'''只有3个进程在工作
任务执行0 14051
任务执行0 14052
任务执行0 14053
任务执行0 14051
任务执行0 14052
任务执行0 14053
任务执行0 14051
任务执行0 14052
任务执行0 14053
任务执行0 14051
'''