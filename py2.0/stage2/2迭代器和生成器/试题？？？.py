def add(a, b):
    return a + b


def t1est():
    for r_i in range(4):
        yield r_i


g = t1est()
for n in [2, 10]:
    g = (add(n, i) for i in g)
print(list(g))  # [20, 21, 22, 23]

'''
2+0
10+1
'''
"""

https://blog.csdn.net/qq_33567641/article/details/81097709
没有给出解释
"""