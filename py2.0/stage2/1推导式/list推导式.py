import random

list_0 = [1, 2, 3, 4]
"""
列表推导式：
"""
# Express: 表达式，用于存放新列表中的元素，即结果；
# var：循环的变量

# 案例1，list=[Express for var in range]   指定范围
list_1 = [random.randint(10, 100) for i in range(5)]
print(list_1)  # 随机的5次：[28, 71, 100, 83, 59]

# 案例2，list=[Express for var in list]    根据表达式，生成新的列表
list2_1 = [i for i in range(5)]  # [0, 1, 2, 3, 4]
list2_2 = [i for i in range(1, 5)]  # [1, 2, 3, 4]
list2_3 = [x * 2 for x in list_0]  # [2, 4, 6, 8]

# 案例3，list=[Express for var in list if condition]   根据表达式和条件，生成新的列表
list3_1 = [x * 2 for x in list_0 if x > 3]  # [8]
list3_2 = [i for i in range(11) if i % 2 == 0]  # [0, 2, 4, 6, 8, 10]
list3_3 = [i * j for i in range(1, 3) for j in range(1, 3)]  # 带2个变量的,[1, 2, 2, 4]

attrValueModeList = [{"a": "", "id": 66}, {"b": "", "id": 77}, {"c": "", "id": 88}]
idList = [i.get("id") for i in attrValueModeList]  # [66, 77, 88]

if __name__ == '__main__':
    print("list_1：", list_1)
    print("list2_1：", list2_1)
    print("list2_2：", list2_2)
    print("list2_3：", list2_3)
    print("list3_1：", list3_1)
    print("list3_2：", list3_2)
    print("list3_3：", list3_3)
