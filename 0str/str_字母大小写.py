string = "runoob.com"
print(string.isalnum())  # 判断所有字符都是数字或者字母
print(string.isalpha())  # 判断所有字符都是字母
print(string.isdigit())  # 判断所有字符都是数字
print(string.islower())  # 判断所有字符都是小写
print(string.isupper())  # 判断所有字符都是大写
print(string.istitle())  # 判断所有单词都是首字母大写，像标题
print(string.isspace())  # 判断所有字符都是空白字符、\t、\n、\r

string = "www.RUNOOB.com"
print(string.upper())  # 把所有字符中的小写字母转换成大写字母
print(string.lower())  # 把所有字符中的大写字母转换成小写字母
print(string.capitalize())  # 把第一个字母转化为大写字母，其余小写
print(string.title())  # 把每个单词的第一个字母转化为大写，其余小写
print(string.swapcase())  # 大小写互换
