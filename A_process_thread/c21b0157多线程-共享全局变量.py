import threading

a = 100


def func1():
    global a  # 不声明的话， a +=1会报错，因为形参没有a
    # todo 但是直接print a可以.
    # 因为这里是修改数据，把a换成列表就不用加global了，因为列表是可变类型的
    # 直接print没有修改数据
    for i in range(1000000):
        a += 1
    print("线程1修改完a:", a)


def func2():
    global a
    for i in range(1000000):
        a += 1
    print("线程2修改完a:", a)


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()
t1.join()
t2.join()

# 预期是1000000+1000000
#线程1修改完a: 1286148
#线程2修改完a: 1343038