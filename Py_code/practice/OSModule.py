#-*-coding=utf-8 -*-
import os
'''
处理文件和目录
os.name/getcwd/listdir/syetem'''
print(os.name)
print(os.getcwd())


#-*-coding=utf-8 -*-
import os
#列出某个文件夹下的所有 case,这里用的是 python，
#所在 py 文件运行一次后会生成一个 pyc 的副本
caselist=os.listdir('C:\\Users\\wb-chenxuanhuai\\Desktop\\$$$\\$0CodeHub0130\\$2PythonCode\\practice')
for a in caselist:
    s=a.split('.')[1] #选取后缀名为 py 的文件
    if s=='py':
        #此处执行 dos 命令并将结果保存到 log.txt
        os.system('C:\\Users\\wb-chenxuanhuai\\Desktop\\$$$\\$0CodeHub0130\\$2PythonCode\\practice\\%s 1>>log.txt 2>&1'%a)
        #os.system(command),执行命令或脚本
'''
listdir列出所有路径=caselist，a在caselist中，a用点分割    
'''