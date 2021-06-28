"""
控制线程切换运行得锁-解释器默认的锁

利用一个时间得阈值去切换线程

或者遇到IO阻塞得时候去切换

多线程之间快速切换执行大大缩短时间就是因为任务在等待，但是CPU不会等待线程，它会去执行别得任务，多线程并发就是大大缩短了等待得时间

具体请参考官方文档--线程:https://docs.python.org/zh-cn/3/faq/library.html?highlight=gil#threads

注意：
    Python语言和GIL没有半毛钱关系，仅仅是由于历史原因在Cpython解释器，难以移除GIL。
    GIL：全局解释器锁，每个线程在执行得过程都需要先获取GIL，保证同一时刻只有一个线程可以执行代码。
    Python使用多线程只能只用一个CPU是因为，最一开始设计Python解释器的人没有想到多核的情况，后面代码设计越多越多，导致很难去修改了，一直到现在。
    有人曾经删除过了GIL锁，但是效果非常差，甚至不如单核;---参考文档:https://www.artima.com/forums/flat.jsp?forum=106&thread=214235
    Python使用 多进程 是可以利用多核CPU资源的.
"""