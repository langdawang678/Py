#-*-coding=utf-8 -*-
import os
#列出某个文件夹下的所有 case,这里用的是 python，
#所在 py 文件运行一次后会生成一个 pyc 的副本
caselist=os.listdir(r'D:\$Bastion201805\$4.自动化\Selenium\test_case')
for a in caselist:
    s=a.split('.')[1] #选取后缀名为 py 的文件
    if s=='py':
        #此处执行 dos 命令并将结果保存到 log.txt
        os.system(r'D:\$Bastion201805\$4.自动化\Selenium\test_case\%s 1>>log.txt 2>&1'%a)

'''python 的 os 模块可以用来操作本地文件，
通过 os.listdir()函数获得指定目录中的内容'''
