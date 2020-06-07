import random
"""
列表推导式
# list=[Express for var in range]   指定范围
# list=[Express for var in list]    根据表达式，生成新的列表  
# list=[Express for var in list if condition]   根据表达式和条件，生成新的列表  
Express:表达式，用于计算新列表的元素
var：循环变量
"""

random_list = [random.randint(10, 100) for i in range(5)]
i = [i for i in range(5)] # [0, 1, 2, 3, 4]
print(random_list)  # [28, 71, 100, 83, 59]


list1 = [1, 2, 3, 4]
new_list = [x * 2 for x in list1]  # [2, 4, 6, 8]
new_list2 = [x * 2 for x in list1 if x > 3] # [8]
