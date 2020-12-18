#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2020/10/23 20:46
# @author：langdawang678

# file_name: test_abc.py
import pytest


def test_1():  # test开头的测试函数
    print("test_1")
    assert 1  # 断言成功

@pytest.mark.me
def test_2():
    print("------->test_2")
    assert 1  # 断言失败
# if __name__ == '__main__':
#        pytest.main("-s  test_abc.py") # 调用pytest的main函数执行测试

def test_3():
    print("test_3")

def test_4():
    print("test_4")

def test_5():
    print("test_5")

if __name__ == '__main__':
    pytest.main(["-s", "-m", "me"])