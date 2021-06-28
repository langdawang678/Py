"""
上面的bug如何解决？
    控制线程的执行，避免同时获取数据
同步
    同步就是协同步调,按预定的先后次序进行运行. "同"的意思不是"一起",而是"协同". 线程A和线程B一块配合.

互斥锁
    线程同步能够保证保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁
    互斥锁为资源设定一个状态：锁定/非锁定
    某个线程要更改共享数据时，先将其锁定，此时资源的状态为"锁定"，其他线程不能更改直到该线程释放了资源，将资源状态变成“非锁定”，其它线程才可以去获取锁，然后再次锁定该资源
    互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性

threading模块中定义了Lock类，可以方便的处理锁定
    创建锁：lock = threading.Lock()
    锁定 ： lock.acquire()
    释放锁 ：lock.release()
注意
    如果这个锁之前是没有上锁的，那么acquire不会阻塞
    如果在调用acquire对这个锁上锁之前，它被其他线程上了锁，那么此时acquire会阻塞，直到这个锁被其他线程解锁为止
    上锁之后多线程执行肯定会变慢
        上锁，释放锁需要时间
        上了锁的代码块等于同步执行，必须执行完锁内的代码块，并释放了锁，其他线程才有机会获取锁去执行。
        等于多线程锁内的代码是同步执行的，在只考虑锁内代码块的执行效率，甚至比单线程还差.

"""


import threading

a = 0


def func1():
    global a  # 不声明的话， a +=1会报错，因为形参没有a
    # todo 但是直接print a可以.
    # 因为这里是修改数据，把a换成列表就不用加global了，因为列表是可变类型的
    # 直接print没有修改数据
    for i in range(1000000):
        l1.acquire()
        a += 1
        l1.release()
    print("线程1修改完a:", a)


def func2():
    global a
    for i in range(1000000):
        l1.acquire()
        a += 1
        l1.release()
    print("线程2修改完a:", a)


l1 = threading.Lock()
l2 = threading.Lock()

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()
t1.join()
t2.join()

# 预期是1000000+1000000
# 线程1修改完a: 1286148
# 线程2修改完a: 1343038
