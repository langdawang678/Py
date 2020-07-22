# 统计字符串中的单词个数
str1 = "this is my first test case, this case is good ,is "

# 一、新建一个str，替换非字母为空格
new_s = ""
for i in str1:
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        new_s = new_s + i
    else:
        new_s = new_s + " "
print(new_s)  # this is my first test case  this case is good  is

# 二、分割新字符串到list中
lists = new_s.split()
print(f"单词数量为{len(lists)}")  # 单词数量为11

# 三、统计list中的单词
max_num = 0
for i in lists:
    if lists.count(i) > max_num:
        max_num = lists.count(i)
        key_word = i
print(f"单词 {key_word} 的数量最多，数量为：{max_num}")
