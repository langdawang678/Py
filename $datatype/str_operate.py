"""
1、字符串翻转（2种）
2、字符串中移除指定位置的字符
3、字符串作为代码执行
"""

# 1、字符串反转
# 方式1
s = "adb"
# reversed(seq) ，seq可以是 tuple, string, list 或 range。 s= reversed(str1)  # 返回一个反转的迭代器。
print(s)  # <reversed object at 0x02A255B0>
print(type(s))  # <class 'reversed'>
print(list(s))  # ['b', 'd', 'a']
string = 'Runoob'
print(''.join(reversed(string)))
# 方式2
string = 'Runoob'
print(string[::-1])

# 2、字符串中移除指定位置的字符
test_str = "Runoob"
# 移除第三个字符 n，索引为2
new_str = ""
for i in range(0, len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]
print("字符串移除后为 : " + new_str)


# 3、字符串作为代码执行
# https://www.runoob.com/python3/python3-func-exec.html
# https://www.runoob.com/python/python-func-eval.html
