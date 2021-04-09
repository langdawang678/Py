
"""dict1 = {key的表达式: value的表达式}"""
list_0 = ["name", "age", "gender"]
dict1 = {list_0.index(i): i for i in list_0}
print(f"列表中元素值为name的元素索引是：{list_0.index('name')}")  # 0
# {0: 'name', 1: 'age', 2: 'gender'}

dict2 = {i: i for i in list_0}
# {'name': 'name', 'age': 'age', 'gender': 'gender'}

if __name__ == '__main__':
    print(dict1)
    print(dict2)

