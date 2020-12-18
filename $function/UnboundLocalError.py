#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2020/12/17 3:43 下午
# @author：langdawang678

code = 2


class UnboundLocalError():
    def mockfunc(self):
        if code == 1:
            env = "daily"
        elif code == 2:
            env = "pre"
        print(env)


if __name__ == '__main__':
    UnboundLocalError().mockfunc()
