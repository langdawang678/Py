# 怎么计算2的3次⽅
2 ** 3
pow(2, 3)
# 怎么找出序列中的最⼤最⼩值？
max([1, 2, 3, 4])



str1 = "good morning"
# 怎么批量替换字符串中的元素
str1.replace("o", "new")
# 怎么把字符串按照空格进⾏拆分
str1.split()  # 返回list，默认按空格分
# 怎么去除字符串⾸位的空格
str1.strip()
# 怎么将字符列表转为字符串
" ".join(["hello", "world"])
# 怎么快速打印出包含所有 ASCII 字⺟（⼤写和⼩写）的字符串
import string
string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# 怎么让字符串居中
str1.center()
# 怎么在字符串中找到⼦串
"i love you ".find("you")  # 返回索引=7
# 怎么让字符的⾸字⺟⼤写，其他字⺟⼩写
str1.title()



list1 = [0, 1, 2]
list2 = [1, 2, 3]
# 怎么清空列表内容
list1.clear()
# 怎么计算指定的元素在列表中出现了多少次？
list1.count("obj")
# 怎么在列表末尾加⼊其它元素
list1.append("obj")
list1.extend(list2)
# extend 和列表相加的区别？
'''extend是扩展原list，相加是新建list'''
# 怎么查找列表中某个元素第⼀次出现的索引，从 0 开始
list1.index("obj")
# 怎么将⼀个对象插⼊到列表中
list1.insert(1, "obj")
# 怎么删除列表中元素
list1.pop(3)  # index=3 默认是最后一个
# 怎么删除列表中指定元素
list1.remove("hi")
# 怎么让列表按相反顺序排列？
list1.reverse()
list1[::-1]


# 怎么表示只包含⼀个元素的元组
tuple1 = (1,)  # 不加逗号为int了

# 怎么给字典中不存在的key指定默认值
d = {'age': 42, 'name': 'g'}
print(d.get('aa', 'fuzhi'))  # fuzhi
print(d.get('aa'))  # None
print(d.get('age'))  # 42

# 怎么快速求 1 到 100 所有整数相加之和
sum(range(1, 100))
# 怎么查出模块包含哪些属性？
dir(str)
dir(str.find)
# 怎么快速查看某个模块的帮助⽂档
str.__doc__
range.__doc__  # 模块.__doc__

# 怎么从⼀个⾮空序列中随机选择⼀个元素？

# 怎么查出通过 from xx import xx导⼊的可以直接调⽤的⽅法？
# 花括号{} 是集合还是字典？
# 怎么求两个集合的并集？
# 求两个集合的交集
# 求两个集合中不重复的元素？
# 求两个集合的差集？
# 从⼀个序列中随机返回 n 个不同值的元素
# 怎么⽣成两个数之间的随机实数
# 怎么在等差数列中随机选择⼀个数
# 怎么在⽂件⾥写⼊字符？
# 怎么读取⽂件内容？
# 怎么把程序打包成 exe ⽂件
# 怎么把程序打包称 Mac 系统可运⾏的 .app ⽂件
# 怎么获取路径下所有⽬录名称？
# Python 环境下怎么执⾏操作系统命令？
# 怎么将当前时间转为字符串？
# 怎么将秒数转为时间数组
# 将时间元组转换为从新纪元后的秒数
# 怎么将字符串转为时间元组
# 怎么随机打乱列表的顺序
# Python进阶习题
# 怎么⽤for循环实现把字符串变成Unicode码位的列表
# 怎么⽤列表推导式实现把字符串变成Unicode码位的列表
# 打印出两个列表的笛卡尔积
# 可迭代对象拆包时，怎么赋值给占位符
# Python3 中，⽤什么⽅式接收不确定值或参数
# ⽤切⽚讲对象倒序
# 怎么查看列表的 ID
# 可变序列⽤*=（就地乘法）后，会创建新的序列吗？
# 不可变序列⽤*=（就地乘法）后，会创建新的序列吗？
# 关于+=的⼀道谜题
# sort() 和 sorted() 区别
# 怎么通过 reverse 参数对序列进⾏降序排列
# numpy 怎么把⼀维数组编程⼆维数组
# 快速插⼊元素到列表头部
# 字典的创建⽅法
# 通过⼀次查询给字典⾥不存的键赋予新值
# 怎么统计字符串中元素出现的个数？
# 列表去重
# 求m中元素在n中出现的次数
# 新建⼀个Latin-1字符集合，该集合⾥的每个字符的Unicode名字⾥都有
# “SIGN”这个单词，⽤集合推导式完成。
# 查询系统默认编码⽅式
# 修改编码⽅式
# ⽤递归实现阶乘
# >>> all([])的输出结果是多少？
# >>> any([])的输出结果是多少？
# 怎么判断对象是否可被调⽤？
# 怎么列出对象的所有属性
# 怎么得到类的实例没有⽽函数有的属性列表
# 函数中，不想⽀持数量不定的定位参数，但是想⽀持仅限关键字参数，参
# 数怎么定义
# 怎么给函数参数和返回值注解
# 不使⽤递归，怎么⾼效写出阶乘表达式
# Python什么时候执⾏装饰器？
# 判断下⾯语句执⾏是否会报错？
# 怎么强制把函数中局部变量变成全局变量
# 闭包中，怎么对数字、字符串、元组等不可变元素更新
# Python2 怎么解决访问外部变量报错的问题
# 测试代码运⾏的时间
# 怎么优化递归算法，减少执⾏时间
# ⽐较两个对象得值（对象中保存的数据）是否相等
# ⽐较两个对象得内存地址 id 是否相等
# 怎么格式化显示对象？
# 复制⼀个序列并去掉后 n 个元素
# Python中怎么定义私有属性。
# 怎么随机打乱⼀个列表⾥元素的顺序
# 怎么判断某个对象或韩式是⼀个已知的类型
# 怎么打印出分数
# + 和 += 区别
# 怎么列出⼀个⽬录下所有的⽂件名和⼦⽂件名
# 怎么返回 1 到 10 的阶乘列表
# 怎么快速拼接字符串和序列形成新的列表
# 进度条显示
