"""
（未找到原因，下面的程序都OK）
做个demo，演示env为什么会报错
UnboundLocalError, local variable 'xxxx' referenced before assignment
"""
code = 2


class UnboundLocalError():
    def mockfunc(self):
        if code == 1:
            env = "daily"
        elif code == 2:
            env = "pre"
        print(env)


if __name__ == '__main__':
    UnboundLocalError().mockfunc()  # pre
