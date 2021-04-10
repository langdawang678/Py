#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2021/3/9 4:45 下午
# @author：langdawang678

"""
https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
结合图去理解和记忆

case1 直接赋值, b=a：
    赋值引用，ab两个变量指向同一个对象。（即对象的引用（别名））
case2 浅拷贝，b=a.copy 或者 b=copy.copy(a)：
    ab两个变量是独立的对象，但他们的子对象还是指向统一对象（是引用）。（即拷贝父对象，不会拷贝对象的内部的子对象。）
case3 深拷贝，b=copy.deepcopy(a)：
    b变量完全拷贝了父对象及其子对象，两者是完全独立的。

记忆：
1.直接赋值，变量是同一个引用，【父子都变】
2.浅拷贝，变量的父对象是独立的，子对象指向同一个引用，【父不变，子变】
3.深拷贝，变量的父和子对象是独立的，【父子都不变】
（这里的"父"指的是"第一级"）
"""
import copy
# 字典的例子***********************************************************
a = {"1": [1, 2, 3]}
case1_1 = a
case1_2a = a.copy()
case1_2b = copy.copy(a)
case1_3 = copy.deepcopy(a)

a[2] = "222"  # 外部(父对象)添加
a["1"].append(4)  # 内部(子对象)添加

print(case1_1)  # {'1': [1, 2, 3, 4], 2: '222'}     直接引用
print(case1_2a)  # {'1': [1, 2, 3, 4]}              父独立，子引用
print(case1_2b)  # {'1': [1, 2, 3, 4]}              父独立，子引用
print(case1_3)  # {'1': [1, 2, 3]}                  父子对象都独立

# 列表的例子***********************************************************
import copy
aa = [1, 2, 3, 4, ['aa', 'b']]  # 原始对象
bb = aa  # 赋值，传对象的引用
cc = copy.copy(aa)  # 对象拷贝，浅拷贝
dd = copy.deepcopy(aa)  # 对象拷贝，深拷贝
aa.append(5)  # 修改对象aa
aa[4].append('c')  # 修改对象aa中的['aa', 'b']数组对象
print('aa = ', aa)  # aa =  [1, 2, 3, 4, ['aa', 'b', 'c'], 5]
print('bb = ', bb)  # bb =  [1, 2, 3, 4, ['aa', 'b', 'c'], 5]

#todo 高亮：  变量cc 是重点，"父对象是独立的，子对象是指向同一个引用"
print('cc = ', cc)  # cc =  [1, 2, 3, 4, ['aa', 'b', 'c']]
print('dd = ', dd)  # dd =  [1, 2, 3, 4, ['aa', 'b']]
