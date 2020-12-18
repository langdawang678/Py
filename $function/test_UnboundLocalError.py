#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2020/12/17 3:52 下午
# @author：langdawang678
from function import UnboundLocalError
# import $function.UnboundLocalError.mock
# import $function.UnboundLocalError

class TestUnboundLocalError:

    def test_1(self):
        UnboundLocalError().mockfunc()

    # def nottest(self):
    #     UnboundLocalError().mockfunc()

if __name__ == '__main__':
    # UnboundLocalError().mock()
    TestUnboundLocalError().nottest()