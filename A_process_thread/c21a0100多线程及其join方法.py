
import time
import threading


def func1():
    for i in range(0, 5):
        time.sleep(1)
        print('....事情1....')  # 耗时5秒


def func2():
    for i in range(6):
        time.sleep(1)
        print('....事情2....')  # 耗时6秒

# t1 = threading.Thread(target=func1())  # 错误示例，这里入参是函数名，不需要括号


def main():

    t1 = threading.Thread(target=func1)  # 调用了Thread类的构造方法，返回了一个线程对象：<Thread(Thread-1, initial)>
    t2 = threading.Thread(target=func2)
    print(t1)  # <Thread(Thread-1, initial)>
    s_time = time.time()
    t1.start()
    t2.start()
    '''若不加join，总耗时为0，主线程直接往下执行，t1 t2子线程相当于异步在执行'''
    # 总耗时0.0010001659393310547秒

    # join()函数，让主线程等待子线程执行完成后再执行（join相当于把主线程阻塞住）
    '''#  1.无参数时，默认等待线程执行完成后再执行主线程，一般都不设定时间'''
    t1.join()  # t2耗时5秒，单独这行时总耗时=5秒，因为不会等t2执行后再执行主线程
    t2.join()  # t2耗时6秒，单独这行时总耗时=6

    '''#  2.设定参数时，时间会叠加, 小于实际耗时时，设定生效，如下的总耗时为4秒'''
    # t1.join(2)
    # t2.join(2)

    '''# 3.设定参数时，时间会叠加, 但大于实际耗时时，以实际耗时为准.如下的总耗时为6秒'''
    # t1.join(10)
    # t2.join(10)

    cost_time = time.time() - s_time
    print(f"总耗时{cost_time}秒")


if __name__ == '__main__':
    main()
