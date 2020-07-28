"""
结论：无return、return 空、return None 的效果相同
解决：函数中rerun后跟变量或表达式，才能返回值
"""
def test1(a):
    print("test")
    return
obj1 = test1(1)  # test
print(obj1)  # None

def test2(b):
    print("test2")
    return b
obj2 = test2(2)  # test2
print(obj2)  # 2

def test3(x, y):
    c = y+1
    return {"a": c, "b": x}  # 返回字典
    ## return c, x  # 返回元组；返回值可以是任意类型
print(test3(6, 9))  # {'a': 10, 'b': 6}

def user4(name4):
    print(f"name4 is :{name4}")
    return
person4 = user4("zhangsan")  # 提示：Function 'user' doesn't return anything
print(person4)  ## None


list5 = [1, 2]
a5 = list5.append("3")
print(f"a5 is: {a5}")  # None
b6 = list5.pop()
print(f"b6 is : {b6}")  # 3


