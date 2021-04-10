"""
python中变量名（变量名就是引用）和对象（对象在内存上创建）是分离的
"""
a = 1  # 赋值语句，整数 1 为一个对象，a 是一个引用，利用赋值语句，引用a指向了对象1
print(id(a))  # 返回int的 内存地址，如，4485692192

a = "banana"
'''内存中建立了一个字符串对象‘banana’，
通过赋值 将 引用a 指向了 ‘banana’，
同时，对象1不在有引用指向它，它会被python的内存处理机制给当我垃圾回收，释放内存。'''
print(id(a))  # 如，140226160246000


# https://www.cnblogs.com/howe670/p/8600851.html
# https://blog.csdn.net/zhuzuwei/article/details/80532963