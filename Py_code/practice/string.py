# coding=utf-8
"""
定义字符串，查看类型，大小写，拼接，尾部去空格，数字转换字符
字符串格式化
"""
# 1. 定义字符串变量var1和var2:
var1 = 'abc def'
var2 = "GHIJ  "

# 2. type(),查看变量的类型:
print('变量类型是：', type(var1))

# 3.大写、小写：
print("全部大写、小写：", var1.upper(), var2.lower())
print('字符串的首字母大写:', var1.capitalize())
print("字符串的每个单词的首字母大写:", var1.title())

# 4.拼接
var3 = var1 + " " + var2
print("var3=", var3 + " !")

# 去除字符串尾部空格
print("var3 rstrip后=" + var3.rstrip())

# 截取(索引&切片)字符串的一部分并与其他字段拼接:
print("已更新字符串 : ", var1[1:4] + 'Runoob! ' + var2)

# 函数str将非字符串的值，转换为字符串
age = 23
print("Happy " + str(age) + "rd Birthday!")

# 字符串格式化

