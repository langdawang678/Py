"""演示
"""
from A_func.UnboundLocalError import UnboundLocalError


class TestUnboundLocalError:

    # pytest测试方法，@@@直接运行这个方法不行
    def test_1(self):
        UnboundLocalError().mockfunc()
        print("test_1")

    # 非pytest测试方法，可调用另一个模板里的方法
    def not_pytest(self):
        UnboundLocalError().mockfunc()
        print("not_pytest")


if __name__ == '__main__':
    # 直接用Python运行，会运行这里的3行代码
    UnboundLocalError().mockfunc()  # pre
    TestUnboundLocalError().not_pytest()  # pre not_pytest
    TestUnboundLocalError().test_1()  # pre  test_1

    '''
        用pytest运行，会运行测试类TestUnboundLocalError 里的test_1这个测试方法，跑1条case。
    前提是 Edit configuration中的pytest里的 script path 添加了这个测试文件
    '''
