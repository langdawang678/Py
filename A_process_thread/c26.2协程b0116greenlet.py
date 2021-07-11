"""为了更好使用协程来完成多任务，
Python中的greenlet模块对 yeild进行封装，
从而使得切换任务变得更加简单"""



'''
使用：创建多任务的greenlet对象
切换：switch()方法传参和任务切换
'''
import greenlet


def work1():
    for i in range(10):
        print("---work1----{}".format(i))
        # 标记切换g2任务
        g2.switch()


def work2():
    for i in range(10):
        print("---work2----{}".format(i))
        # 标记切换g1任务
        g1.switch()


# 创建两个greenlet对象
g1 = greenlet.greenlet(work1)
g2 = greenlet.greenlet(work2)

# 切进任务1，有参数可以传参数 *args, **kwargs
g1.switch()  # 类似于 生成器的next
