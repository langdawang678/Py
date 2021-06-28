import threading

# 全局变量，利用多线程
# 对a进行+1 ，两千万次，一个线程加已一千万次
import time

a = 0


def fun_1(lock):
    global a
    for i in range(1000000):
        # 修改前上锁
        lock.acquire()
        a += 1
        # 修改完释放锁
        lock.release()
    print("线程1修改完a={}".format(a))


def fun_2(lock):
    global a
    for i in range(1000000):
        # 修改前上锁
        lock.acquire()
        a += 1
        # 修改完释放锁
        lock.release()
    print("线程2修改完a={}".format(a))


def main():
    # 创建锁
    lock = threading.Lock()

    # 建立两个线程,把锁传进任务上锁
    s_time = time.time()
    t1 = threading.Thread(target=fun_1, args=(lock,))
    t2 = threading.Thread(target=fun_2, args=(lock,))

    t1.start()
    t2.start()

    # 等待子线程执行完毕
    t1.join()
    t2.join()
    e_time = time.time()
    print("最后修改完a={}".format(a))
    print("最后修改完得时间:{}".format(e_time - s_time))

    #
    # 锁后时间：


if __name__ == '__main__':
    main()
    """
    上锁前：
    线程2修改完a = 1269517
    线程1修改完a = 1302318
    最后修改完a = 1302318
    时间：0.15441060066223145

    上锁后：
    线程2修改完a=1976899
    线程1修改完a=2000000
    最后修改完a=2000000
    时间:1.1480515003204346

    """