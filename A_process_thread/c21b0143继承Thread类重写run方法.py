"""
# 通过继承Thread类并重写run方法,实现多线程

注意点:
1/线程启动start方法就是运行了run方法,重写run方法完成任务
2/创建线程时不需要在传任务函数
3/如果任务函数需要参数，需要重写init方法，并返回父类init方法
"""
import threading
import requests


class Test(threading.Thread):
    def __init__(self, url):  # 重写run方法时,需要参数时,必须用到父类的__init__方法.因为init干了很多事情
        self.url = url
        super().__init__()

    def run(self):
        print("run")
        res = requests.get(self.url)
        print(res)


t = Test("https://www.baidu.com")
t.start()
