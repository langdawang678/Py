"""先演一下，"斐波那契数列"是什么"""

# 斐波那契数列，0开始
n = 10
if n == 1:
    print(0)
else:
    a = 0
    b = 1
    count = 1
    print(a, end=" ")
    while count < n:
        c = a + b
        a = b
        b = c
        count = count + 1
        print(a, end=" ")
# 0 1 1 2 3 5 8 13 21 34


# 递归对时间和空间要求高，n越大要求的时间和空间越大，因此效率极低，不建议使用
def ab(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n >= 3:
        return ab(n - 1) + ab(n - 2)


print(ab(10))

print("从1开始:  ", end='')
n = 10
if n == 1:
    print(1)
else:
    a = 1
    b = 2
    count = 1
    print(a, end=" ")
    while count < n:
        c = a + b
        a = b
        b = c
        count = count + 1
        print(a, end=" ")

print()


def ab(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n >= 3:
        return ab(n - 1) + ab(n - 2)


print(ab(10))
