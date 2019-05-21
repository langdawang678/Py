year = int(input("输入一个年份: "))
    #input后需要类型转换？
if(year%4==0 and year%100!=0 or year%400==0):
    #四年一闰；百年不闰，四百年再闰.
    print("%d年是闰年" %year)
else:
    print("'%d'不年是闰年" %year)
 
'''
if(1 and 1 or 0):
    print("true")
else:
    print("false")
'''
