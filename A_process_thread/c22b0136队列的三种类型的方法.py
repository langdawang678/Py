"""
Queue.qsize() : 返回当前队列包含的消息数量
Queue.empty() : 队列为空返回True，反之False
Queue.full() : 队列满了返回True,反之False
Queue.get(self,block=True,timeout=None) : 获取队列中的值
    timeout (block=True) ：队列内为空，get值的等待时间，时间内等不到报错，默认一直等
    block : True：队列为空等待获取值，False：队列为空报错停止执行线程
Queue.put(self,block=True,timeout=None) : 写入队列
    timeout(block=True) ：队列满了写入队列值的等待时间，等待时间后还是满的报错，默认一直等待
    block : True：队列满了等待写入值，False：队列满了报错停止执行线程
Queue.get_nowait() : 相当于Queue.get(False)
Queue.put_nowait() : 相当于Queue.put(False)
Queue.task_done() : 在完成一项工作之后，使用该方法，可以向队列发送一个信号，表示该任务执行完毕
Queue.join() 实际上意味着等待队列种多有的任务执行完之后，在往下执行，否者一直等待
    任务执行完毕，意味着着收到了Queue.task_done()这个信号
    如果用了join方法，没有发送信号会一直等待
    put了多少个数据，在get使用之后，就的发送多少个Queue.task_done() 使用完毕的信号，不然也会一直等待
    如果发送的Queue.task_done()信号，比put的个数多，会报错
"""
import queue

# 三种队列
# 1.先进先出
q = queue.Queue(3)
q.put(1)
q.put(11)
q.put(11)
# q.put(22) # 不加block就会一直卡住
# q.put(22, block=False)  # 不等待,报错raise Full
# q.put_nowait(22)  # 不等待,报错raise Full

# 获取队列中的任务数
print(q.qsize())  # 3
# 判断队列是不是满了
print(q.full())  # True
q.task_done()
q.task_done()
q.task_done()

# 判断队列是否为空,数据get完了就空了
print(q.empty())  # False

# 队列中的任务是否执行完毕
q.join()  # 没有对应数量的task_done信号时,一直等待.
print("join之后的代码")

# 2.后进先出
q2 = queue.LifoQueue()
'''继承了Queue,所以方法也相同'''

# 3.优先级
q3 = queue.PriorityQueue()
'''继承了Queue,所以方法也相同'''
q3.put(22, "222")
q3.put(1,"hhh")
q3.put(100, 100)
print(q3.get())