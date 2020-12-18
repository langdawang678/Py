# coding:utf-8
file_name = "basic_write_and_read.txt"
# 写文件
with open(file_name, "w") as out_file:
    out_file.write("新建文件并写入字符串。\n换个行吧。")
    out_file.close()

# 读文件read()，返回str
fp = open(file_name, "r")
text_read = fp.read()
print(f"read()函数返回的类型是：{type(text_read)}")  # <class 'str'>
print(text_read)
fp.close()

# 读文件readlines()，返回list
fp = open(file_name, "r")
text_readlines = fp.readlines()
print(f"readlines()函数返回的类型是：{type(text_readlines)}")  # <class 'list'>
print(text_readlines)
fp.close()