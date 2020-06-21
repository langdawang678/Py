"""
1、质数
2、阶乘
3、闰年
4、最大公约数
5、最小公倍数
"""
# 判断质数
'''除了1和它本身外，不能被其他自然数（质数）整除'''
for i in range(1, 100):
    for j in range(2, i):
        if i % j == 0:
            print("i=%d" % i, "not zhishu")
            break

#  阶乘
'''
整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积.
0的阶乘为1。即：n!=1×2×3×...×n。
'''
# num = int(input("input a int:"))
num = 4
if num == 0:
    print("0的阶乘是1")
else:
    x = 1
    for i in range(1, num + 1):
        x = x * i
    print("%d 的阶乘为 %d" % (num, x))

# 闰年
'''四年润 and 百年不润 or 四百年再润'''
# year = int(input("输入一个年份: "))
year = 2020
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    # 四年一闰；百年不闰，四百年再闰.
    print("%d年是闰年" % year)
else:
    print("'%d'不年是闰年" % year)
