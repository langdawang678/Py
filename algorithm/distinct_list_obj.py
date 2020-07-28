# 列表去重

# 方法1，set
list1 = [11, 22, 33, 44, 11, 22]
print(set(list1))

# 方法2，not in
list2 = [11, 22, 33, 44, 11, 22]
new_list = []
for i in list2:
    if i not in new_list:
        new_list.append(i)
print(new_list)
