"""

https://blog.csdn.net/u012609509/article/details/72911564
"""


class Sample:
    def __enter__(self):
        print("in __enter__")
        return "Foo"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("in __exit__")


def get_sample():
    return Sample()


with get_sample() as sample:
    print("Sample: ", sample)

'''
打印:
in __enter__
Sample:  Foo
in __exit__

可以看到，整个运行过程如下：
（１）enter()方法被执行；
（２）enter()方法的返回值，在这个例子中是”Foo”，赋值给变量sample；
（３）执行代码块，打印sample变量的值为”Foo”；
（４）exit()方法被调用；
'''