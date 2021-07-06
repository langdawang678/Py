"""
进程类里的方法,和线程的类似:

Process(group=None, target=None, name=None, args=(), kwargs={})
  target: 给子进程传递执行的任务代码
  args：给target指定的函数传递参数，元组方式
  kwargs：给target指定的函数传递参数，字段方式
  name：给进程设置一个名字
  group：指定进程组，大多数情况下用不到

Process实例的常用方法
  start() ：启动子进程实例
  is_alive() ：判断子进程是否还在活着
  join(timeout) ：是否等待子进程执行结束，或者等待多少
  terminate() ：不管任务是否完成，立即终止子进程

Process实例对象常用的属性
  name ：当前进程的名字
  pid ：当前进程的pid（进程号）
  主进程中可以进程p.pid获取
  子进程中用os.getpid()获取

"""
import time
from multiprocessing import Process

a = 100  # 因为进程之间不共享资源(全局变量),所以对a各自进行操作(在不同的内存空间).


def work1():
    global a
    for i in range(3):
        a += 1
        print(f"这个是 任务1-----{a}")
        time.sleep(0.5)


def work2():
    global a
    for i in range(3):
        a += 100
        print(f"这个是 任务2-----{a}")
        time.sleep(0.5)


if __name__ == '__main__':
    '''
    # PYTHON使用多进程MULTIPROCESSING进行做处理的时候报FREEZE_SUPPORT错误的解决方法
    https://www.freesion.com/article/2458937949/  (multiprocessing根据平台不同会执行不同的代码：在类UNIX系统下由于操作系统本身支持fork()语句)
    
    在windows上，子进程会自动import启动它的这个文件，
    而在import的时候是会自动执行这些语句的。
    如果不加__main__限制的化，就会[无限递归]创建子进程，进而报错。
    '''
    p1 = Process(target=work1)
    p2 = Process(target=work2)

    p1.start()
    p2.start()

'''
这个是 任务1-----101
这个是 任务2-----200
这个是 任务1-----102
这个是 任务2-----300
这个是 任务1-----103
这个是 任务2-----400
'''