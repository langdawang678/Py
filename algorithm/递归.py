#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2021/4/28 4:46 下午
# @author：langdawang678

def fun(n):
    if n==1:
        return 1
    else:
        return n * fun(n-1)
print(fun(1))
print(fun(4))