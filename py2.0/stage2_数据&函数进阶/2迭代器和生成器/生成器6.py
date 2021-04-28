#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2021/4/28 4:23 下午
# @author：langdawang678
def gen():
    for i in range(5):
        j = yield i
        print(j)
g = gen()
print(g.__next__())  # 0
print(g.__next__())  # None  1
print(g.__next__())  # None  2
print(g.send(666))  # 666 3
'''
0
None
1
None
2
666
3
'''