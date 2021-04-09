# 生成器好处：本地调用节约内存空间
"""
# 1000套衣服的list
def cloth():
    lst = []
    for i in range(0, 1000):
        lst.append("学校衣服" + str(i))
    return lst
cl = cloth()
print(cl)
"""

'''这1000套衣服一次性拿到手还得占内存空间，造成了很多浪费。
最好的方法就是我需要多少就是多少，直接根据需求来。
这时，我们就需要一个生成器'''
def cloth():
    for i in range(0, 10000):
        yield "学校衣服" + str(i)
cl = cloth()
print(cl.__next__())  # 学校衣服1
print(cl.__next__())  # 学校衣服2
print(cl.__next__())  # 学校衣服3
print(cl.__next__())  # 学校衣服4