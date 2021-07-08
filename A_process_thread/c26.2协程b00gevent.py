import gevent

"""
协程：gevent，
对greenlet的再次封装
协程存在于线程之中，线程默认不会等等待协程执行的
"""
'''
gevent.spawn(*args, **kwargs)
    创建并开启协程
    第一个参数传任务函数
    其他参数依次传入即可
gevent.sleep()
    切换的标志
    gevent里等待方法
gevent().join()
    线程等待协程的方法
'''


def work1(a):
    for i in range(10):
        print("---work{}----{}".format(a, i))
        # 切换的标志
        gevent.sleep(0.001)


def work2(a):
    for i in range(10):
        print("---work{}----{}".format(a, i))
        # 切换的标志
        gevent.sleep(0.001)


# 创建两个gevent对象
# 参数*args, **kwargs
# 默认就已经开启执行了
g1 = gevent.spawn(work1, a=1)
g2 = gevent.spawn(work2, a=2)

# 线程等待协程执行完
g1.join()
g2.join()
