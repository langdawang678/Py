from collections import namedtuple

'''https://www.cnblogs.com/ljhdo/p/10656314.html'''
User = namedtuple('User1', ['name', 'age', 'id'])
print(type(User))
# 通过类方法 _make() 和一个list创建一个User对象
# 类方法 _make(iterable)：接受一个可迭代对象来生产这个类的实例
user = User._make(['Runoob', 'male', 12])
print(type(user))
user = User('Runoob11', 'male11', 1211)
print(type(user))

print(User._fields)  # 类属性 _fields：包含这个类所有字段名的元组
print(user.age)


user = user._replace(age=22)  # User(name='user1', sex='male', age=22)
print(user.age)



# 命名元组在存储csv或者sqlite3返回数据的时候特别有用
