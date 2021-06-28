"""
“创建一个线程类，每个线程对xx地址发送100个请求，开启10个线程，同时发送。计算总的耗时，分析平均每个请求所需要的时间”
"""
import threading
import time

import requests


class TestThread(threading.Thread):
    def run(self):
        for i in range(10):
            requests.post("http://httpbin.org/post")


thread_list = []
time1 = time.time()
for i in range(10):
    t = TestThread()
    thread_list.append(t)  # 创建10个线程对象

# 遍历线程对象,开启线程
for i in thread_list:
    i.start()

# 遍历线程对象,让主线程等待子线程结束之后再往下执行
for i in thread_list:
    i.join()
time2 = time.time()
print(time2 - time1)
