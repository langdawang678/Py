"""
# 10000个请求,开启2个进程，每个进程中实现3个线程，每个线程中实现5个协程去处理 计算时间
# 共30个协程
"""
import time
import threading
from multiprocessing import Process, Pool, Queue
import gevent
import requests
from gevent import monkey

monkey.patch_all()  # 源码中建议只在 单线程中使用会有很多报错 .


def green_work(q, gname):
    """
    每个协程的工作函数
    :param q:
    :param gname:
    :return:
    """
    count = 0
    while not q.empty():
        try:
            url = q.get(timeout=0.01)  # 避免获取数据时, 其他进程/线程正在占用, 因为队列自带锁
            # 超过等待0.01秒后还是拿不到,表明没数据了或者还是被其他人占用着,会有异常报错
        except:
            pass
        requests.get(url)
        gevent.sleep(0.001)
        count += 1
    print('-----协程{}执行了个{}任务'.format(gname, count))


def thread_work(q, tname):
    """
    每个线程的执行任务函数,在该线程中开启5个协程
    :param q:
    :param tname:
    """
    g_list = []
    for i in range(5):
        gname = f'{tname}-g-{i}'
        print(f"创建协程{gname}")
        g = gevent.spawn(green_work, q, gname)
        g_list.append(g)
    gevent.joinall(g_list)  # 入参是列表, 会等待列表里的协程都完成后,再往下执行


def process_work(q, pname):
    """
    每个进程执行的任务函数,在该进程中开启3个进程
    创建三个线程
    :param q: 进程间通讯的任务队列
    :param pname:标识是哪个进程
    :return :
    """
    # print(f'{pname}该进程的任务数为{q.qsieze()}')
    # 创建三个线程,并执行
    thread_list = []
    for i in range(3):
        tname = f'{pname}-th-{i}'
        print(f'创建线程{tname}')
        t = threading.Thread(target=thread_work, args=(q, tname))
        thread_list.append(t)
        t.start()

    # 让主线程阻塞, 等待子线程
    for t in thread_list:
        t.join()


# 计时装饰器
def count_time(func):
    def wrapper(*args, **kwargs):
        print("开始执行")
        t1 = time.time()
        func(*args, **kwargs)
        print("执行结束")
        t2 = time.time()
        print("执行时间", t2 - t1)
        return t2 - t1

    return wrapper


# 主流程在main函数里,用来控制程序的运行
@count_time
def main():
    # 创建10000个请求的队列
    q = Queue()

    for i in range(10000):
        q.put("http://127.0.0.1:5000")
    # 开启两个进程处理
    print(f"队列创建完成,数量{q.qsize()}")
    pro_list = []
    for i in range(2):
        pname = f'pro-{i}'
        print(f"创建进程{pname}")
        p = Process(target=process_work, args=(q, pname))  # 把进程名也传递给process_work函数,方便看是哪个进程
        p.start()
        pro_list.append(p)
    # 让主进程等在子进程执行结束再往下执行
    for p in pro_list:
        p.join()


if __name__ == '__main__':
    main()
