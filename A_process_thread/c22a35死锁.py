"""
如果多线程存在多把锁
线程1获取了锁1，还要在获取了锁2才能执行
线程2获取了锁2，还要在获取锁1才能执行
此时，任务1就等着任务2去释放了锁2，才有机会执行
任务2就等着任务1释放了锁1，才有机会执行
最后导致互相等对方释放锁，导致死锁
"""
from threading import Lock, Thread

mutex_a = Lock()
mutex_b = Lock()


class Mythread(Thread):
    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):
        mutex_a.acquire()
        print("get a")
        mutex_b.acquire()
        print("get b")
        mutex_b.release()
        mutex_a.release()

    def fun2(self):
        mutex_b.acquire()
        print("get B")
        import time
        time.sleep(2)
        mutex_a.acquire()
        print("get A")
        mutex_a.release()
        mutex_b.release()


if __name__ == '__main__':
    for i in range(8):
        thread_test = Mythread()
        thread_test.start()


"""
解释如下
#死锁产生原因 首先线程1 抢到A锁 其他抢不到等着，接着抢到B锁 其他任然抢A
#接着释放B锁，别的进程任然抢A接着释放A锁，别的进程抢到A锁，线程1抢到B锁，然后睡了2秒
#其他要抢B锁，B锁在线程1上，然后线程1要抢A锁，A锁在线程2上，索要之锁都在别的线程中，所以死锁
"""