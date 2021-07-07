import queue
from multiprocessing import Queue, Manager

# 线程的队列(只能在一个进程中使用)
q = queue.Queue()

# 进程的队列(可在多个进程之间通信)
q2 = Queue()

# 进程池中的队列(给进程池中的各个进程之间使用)
q3 = Manager().Queue()