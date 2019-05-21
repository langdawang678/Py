'''
1、单个if
2、if+ else(可省略)
3、if+ elif(单个或多个)+...+else(可省略)
4、多个if
'''

a=59
if a<10:
    print('case1')
elif a<20:
    print('case2')
elif a<40:
    print('case4')
elif a<60:
    print('case6')
else:
    print('case100-60')
#多个if
if a==59:
    print("a==59")
