"""
知识点：
1、格式化输出的3种写法
2、切片
3、切片后list的+号拼接
"""
# 约瑟夫生者死者小游戏
a = list(range(1, 31))
while len(a) > 15:
    print(f'{a[8]}号下船了')
    print('{}号下船了'.format(a[8]))
    print('%d号下船了' % (a[8]))
    # print(a[:8])
    # print(a[9:])
    a = a[9:] + a[:8]
    # print(a)


# 写成函数
def yuesefu(total, step, rest):
    a = list(range(1, total + 1))
    while len(a) > rest:
        print(f'{a[step - 1]}号下船了')
        a = a[step:] + a[:step - 1]

# 其他的写法
# https://www.runoob.com/python3/python-joseph-life-dead-game.html
