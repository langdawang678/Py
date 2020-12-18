"""
注意:
1/函数实参的调用方式 test(1, 2, 3, 4, a=1, b=2,c=3)
2/函数的（）里才有* 或者**号
3/可以把对象作为*或者**传入
"""


def test(arg, *args, **kwargs):
    print("-------------")
    total = 0
    total = total + arg
    for i in args:
        total = total + i

    print(f"arg={arg}, args={args}, kwargs={kwargs}")
    # print(type(arg), type(args), type(kwargs))  # <class 'int'> <class 'tuple'> <class 'dict'>
    return total


test(1, 2, 3, 4, a=1, b=2, c=3)  # 1 (2, 3, 4) {'a': 1, 'b': 2, 'c': 3}
test(1, 2, 3, 4)  # 1 (2, 3, 4) {}
a = test(1, 2, 3, 4)
print(a)  # arg=1, args=(2, 3, 4), kwargs={}  # 10

# 可以把对象作为*或者**传入
rest = (5, 5)  # 这里的rest可以是元组和列表，会自动脱衣服。
## 集合也可以，但是元素位置不一定，结果可能会不符合预期。
print(test(1, 2, *rest))  # arg=1, args=(2, 5, 5), kwargs={}  # 13

# 可以把对象作为*或者**传入
dict = {"a": 1, "b": "22"}
print(test(1, 2, 3, **dict))  # arg=1, args=(2, 3), kwargs={'a': 1, 'b': '22'}  # 6
