
# 创建一个队列,添加10个任务
# 多进程之间的通信问题

import os
import time
import requests
# from queue import Queue  # 无法实现进程间的通信,他只能在一个进程中用.
'''原理c24a26分后开始讲:
multiprocessing中的Queue,会在不同进程,用同一个参数做关联(给他们共同的一个队列对象q)
'''
from multiprocessing import Process, Queue

a = 1


def work1(q1):
    while q1.qsize() > 0:
        global a
        url = q1.get()
        # requests.get(url)
        time.sleep(1)
        print("work1, 进程{},a ={},url ={}:".format(os.getpid(), a, url))
        a += 1


def work2(q1):
    while q1.qsize() > 0:
        global a
        url = q1.get()
        # requests.get(url)
        time.sleep(1)

        print("work2, 进程{},a ={},url ={}:".format(os.getpid(), a, url))
        a += 1


if __name__ == '__main__':
    q = Queue()
    for i in range(10):
        q.put("http://127.0.0.1")
    # 多进程一定要: 将队列对象参数传进任务函数.
    # (如果这里不传args, work1和2函数的形参无q, 那么work1和2还是各自执行10次,等于没用多进程)
    p1 = Process(target=work1, args=(q,))
    p2 = Process(target=work2, args=(q,))
    p1.start()
    p2.start()

'''
输出:
work1, 进程7160,a =1,url =http://127.0.0.1:
work2, 进程7876,a =1,url =http://127.0.0.1:
work1, 进程7160,a =2,url =http://127.0.0.1:
work2, 进程7876,a =2,url =http://127.0.0.1:
work1, 进程7160,a =3,url =http://127.0.0.1:
work2, 进程7876,a =3,url =http://127.0.0.1:
work1, 进程7160,a =4,url =http://127.0.0.1:
work2, 进程7876,a =4,url =http://127.0.0.1:
work1, 进程7160,a =5,url =http://127.0.0.1:
work2, 进程7876,a =5,url =http://127.0.0.1:

注意:
因为没有真实请求,所以直接print(没有sleep一秒时),直接就1个进程打印完了......
work1, 进程6996,a =0,url =http://127.0.0.1:
work1, 进程6996,a =1,url =http://127.0.0.1:
work1, 进程6996,a =2,url =http://127.0.0.1:
work1, 进程6996,a =3,url =http://127.0.0.1:
work1, 进程6996,a =4,url =http://127.0.0.1:
work1, 进程6996,a =5,url =http://127.0.0.1:
work1, 进程6996,a =6,url =http://127.0.0.1:
work1, 进程6996,a =7,url =http://127.0.0.1:
work1, 进程6996,a =8,url =http://127.0.0.1:
work1, 进程6996,a =9,url =http://127.0.0.1:
'''
