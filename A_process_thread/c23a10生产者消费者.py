"""
用多线程+队列实现:

1.用一个队列存储商品
2.创建一个专门生产商品的对线程类,当商品数少于50时,开始生产,每次生产200个.每生产完一轮暂停1秒.
3.创建一个专门消费商品的对线程类,大于10开始消费,循环消费,每次消费三个,商品小于10暂停2秒

# 1、用一个队列来存储商品
# 2、创建一个专门生产商品的线程类，当商品数量少于50时，开始生产商品，每次生产200个商品，每生产完一轮 暂停1秒
# 3、创建一个专门消费商品的线程类，当商品数量大于10时就开始消费，,循环消费，每次消费3个。当商品实例少于10的时候，暂停2秒
# 4、创建一个线程生产商品，5个线程消费商品

"""
import queue
import time
import threading

q = queue.Queue(250)


class Producer(threading.Thread):
    """生存商品"""

    def run(self):
        count = 0
        while True:
            if q.qsize() < 50:
                for j in range(200):
                    goods = f"第{count}个商品"
                    q.put(goods)
                print('生产完的数量:', q.qsize())
                time.sleep(1)


class Consumer(threading.Thread):
    """消费商品"""

    def run(self):
        while True:
            if q.qsize() > 10:
                for j in range(3):
                    q.get()
                print('消费完的数量:', q.qsize())
            else:
                time.sleep(2)


if __name__ == '__main__':
    # 创建一个线程生产商品
    p = Producer()

    # 开启线程
    p.start()

    # 创建消费者
    for i in range(5):
        c = Consumer()
        c.start()
