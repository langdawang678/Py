#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2020/9/22 8:01 下午
# @author：langdawang678

import pytest


# 1
def setup_module():
    print("\nsetup_module，只执行一次，当有多个测试类的时候使用")
def teardown_module():
    print("\nteardown_module，只执行一次，当有多个测试类的时候使用")


# 被测试方法，
'''验证：函数级（setup_function/teardown_function）仅对函数用例生效。
（即不在类中，每个函数执行一次）'''
def test_function():
    print("测试用例，test_function，不在类中的测试方法")


class TestPytest1(object):

    # 2
    @classmethod
    def setup_class(cls):
        print("\nsetup_class in TestPytest1，只执行一次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class in TestPytest1，只执行一次")

    # 3
    def setup(self):
        print("\nsetup，只执行一次")

    def teardown(self):
        print("\nteardown，只执行一次")

    # ？
    def setup_method(self):
        print("\nsetup_method1，每个测试方法都执行一次")
    def teardown_method(self):
        print("\nteardown_method1，每个测试方法都执行一次")

    # ？
    def setup_function(self):
        print("\nsetup_function,仅对函数用例生效（即不在类中，每个函数执行一次）")
    def teardown_function(self):
        print("\nteardown_function,仅对函数用例生效（即不在类中，每个函数执行一次）")

    # 被测试方法
    def test_1(self):
        print("测试用例，1")

    def test_2(self):
        print("测试用例，2")


class TestPytest2(object):

    @classmethod
    def setup_class(cls):
        print("\nsetup_class in TestPytest2，只执行一次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class in TestPytest2，只执行一次")

    def setup_method(self):
        print("\nsetup_method in TestPytest2，每个测试方法都执行一次")

    def teardown_method(self):
        print("teardown_method in TestPytest2，每个测试方法都执行一次")

    def test_3(self):
        print("测试用例，3")

    def test_4(self):
        print("测试用例，4")


if __name__ == '__main__':
    pytest.main(['-s', 'test_PytestDemo.py'])  # 输出详情，包含打印setup和teardown里的内容
    # pytest.main()  # 不指定文件，当前路径下的test开头的都被执行
    # pytest.main(['-q', 'test_PytestDemo.py'])  # 简化的，只有点和成功率
    # pytest.main(['-v', 'test_PytestDemo.py'])  # 显示文件::类::测试方法
