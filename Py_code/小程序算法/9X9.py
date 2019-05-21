for i in range (1,10):
    for j in range (1,i+1):
        print('{}*{}={}'.format(j,i,j*i),end='\t')
    print()

    #这个print，用于换行，print自带换行效果


'''
\r : 回车,return
\n ：换行,line
\t : 水平制表符


end=""
    1、使print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串。

    2、end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符

    #for i in range (1,10):
        print(i,end=",")

     1,2,3,4,5,6,7,8,9,

    3、这个只有3版本有用。2.*版本不支持。
'''
#format的{}中不能带空格
