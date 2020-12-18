#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2020/9/22 8:01 下午
# @author：langdawang678

import pytest


# 1
def setup_module():
    print("\n\nsetup_module，只执行一次，不放在测试类里，当有多个测试类的时候使用\n")


def teardown_module():
    print("\nteardown_module，只执行一次，不放在测试类里，当有多个测试类的时候使用\n")


# 5 函数级（setup_function/teardown_function）仅对函数用例生效。
def setup_function():
    print("setup_function,仅对函数用例生效（即不在类中，每个函数执行一次）")


def test_function1():
    print("  函数测试用例1，test_function1，不在类中的测试方法")


def test_function2():
    print("  函数测试用例2，test_function1，不在类中的测试方法")


def teardown_function():
    print("\nteardown_function,仅对函数用例生效（即不在类中，每个函数执行一次）\n")


class TestPytest1(object):
    # a
    @classmethod
    def setup_class(cls):
        print("setup_class in TestPytest1，一个测试类执只行一次")

    @classmethod
    def teardown_class(cls):
        print("teardown_class in TestPytest1，一个测试类执只行一次")

    # b
    def setup_method(self):
        print("  setup_method，每个测试方法的最开始，都执行一次")

    def teardown_method(self):
        print("  teardown_method，每个测试方法的最后，都执行一次\n")

    # c
    def setup(self):
        print("    setup，每个方法调用前")

    def teardown(self):
        print("\n    teardown，每个方法调用后")

    # 被测试方法
    def test_1(self):
        print("      测试用例，1")

    def test_2(self):
        print("      测试用例，2")


class TestPytest2(object):
    @classmethod
    def setup_class(cls):
        print("\nsetup_class in TestPytest2，一个测试类执只行一次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class in TestPytest2，一个测试类执只行一次")

    # 被测试方法
    def test_3(self):
        print("测试用例，3")

    def test_4(self):
        print("\n测试用例，4")


if __name__ == '__main__':
    pytest.main(['-s', 'setupteardown.py'])  # 输出详情，包含打印setup和teardown里的内容
    # pytest.main()  # 不指定文件，当前路径下的test开头的都被执行
    # pytest.main(['-q', 'setupteardown.py'])  # 简化的，只有点和成功率
    # pytest.main(['-v', 'setupteardown.py'])  # 显示文件::类::测试方法
