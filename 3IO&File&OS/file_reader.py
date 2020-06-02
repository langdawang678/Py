with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    '''关键字with 在不再需要访问文件后将其关闭。'''
    '''调用了open() ， 但没有调用close() ； 
    1/如果程序存在bug， 导致close() 语句未执行， 文件将不会关闭,可能会导致数据丢失或受损。 
    2/如果在程序中过早地调用close() ， 你会发现需要使用文件时它已关闭 （无法访问） ,导致更多的错误。 '''

    print(contents.rstrip())
    '''貌似没用：read() 到达文件末尾时返回一个空字符串， 而将这个空字符串显示出来时就是一个空行。
    在print 语句中使用rstrip() 删除（剥除） 字符串末尾的空白。'''