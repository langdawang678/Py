"""
方法内调用和修改外部的变量时
"""
# 1方法内直接调用全局变量（非修改）
name1 = "111"
def test1():
    print(name1)  # 111
test1()


# 2方法内的变量重名时
name2 = "111"
def test2():
    name2 = "222"  ## 提示“shadows name 'xxxx' from outer scope”
    '''
    外部有个相同名称的变量在方法内部被重新指定了新的值，
    也就是说你在外部的相同名称的变量压根就没有任何作用
    注意：这里的name和外面的name不是同一个变量，提示操作：rename
    '''
    print(name2)  # 222
test2()


# 3方法内修改外部的变量，会报错，要在内部加global
name3 = "333"
def test3():
    ## name3 = name3+"bbb"  # 红线，提示“Unresolved reference 'name2' ”
    # 运行报错"local variable 'name2' referenced before assignment"
    '''
    原因：这里的name是外边的变量，只能访问，不能修改，要修改加global
    '''
    global name3  ## global表示这里引用的是外部的全局变量name3
    name3 = name3+"global"
    print(name3)  # 333global
test3()
print(name3)  ## 333global ，因为在函数内被改变了
## global不建议使用，容易造成数据混乱