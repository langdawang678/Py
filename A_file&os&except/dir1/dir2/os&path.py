
import os
print(__file__)
# D:/PycharmProjects/Py/$file&os&except/dir1/dir2/os&path.py

print(os.getcwd())
# D:\PycharmProjects\Py\$file&os&except\dir1\dir2

print(os.path.abspath("os_os.path_demo.py"))
# D:\PycharmProjects\Py\$file&os&except\dir1\dir2\os_os.path_demo.py

# 不太实用用：
print(os.path.dirname("/dir1/dir2/os&path.py"))
# "/dir2/os&path.py">>>/dir2
# "/dir1/dir2/os&path.py">>>/dir1/dir2
# 这个比较特殊，入参path中是什么目录(不含文件)，就返回往前的目录