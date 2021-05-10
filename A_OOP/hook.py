"""
https://cloud.tencent.com/developer/article/1761121?from=information.detail.python%E9%92%A9%E5%AD%90%E5%87%BD%E6%95%B0

有了解过，大致的意思是：
1、钩子函数是一种编程机制，和语言无法。
2、hook函数是流程中预定义好的一个步骤，没有实现。
3、调用方 挂载或者注册时， 流程执行就会执行这个钩子函数。

好处：
1、hook设计方式带来灵活性，如果流程中有一个步骤，你想让调用方来实现，你可以用hook函数。

回调函数和hook函数功能上是一致的。
（hook和挂载、注册，是同一个意思）

案例分析：
钩子方法就是上面的register_method_hook方法，
这样的方式可以在 调用方中，自己去调用hook函数（注册），判断是否被注册了，来执行相关的操作，而不用再去调用的代码里去写if语句。

"""


class HookMethodClass(object):

    def __init__(self):
        self.hook_method = None

    def register_method_hook(self, method):
        self.hook_method = method

    def play(self):
        if self.hook_method == None:
            print("未接受到注册方法")
        else:
            print("接受到了方法")
            self.hook_method()


def hooked_method():
    print("我是一个业务方法，需要注册使用")


if __name__ == "__main__":
    hooka = HookMethodClass()
    hooka.register_method_hook(hooked_method)
    hooka.play()

