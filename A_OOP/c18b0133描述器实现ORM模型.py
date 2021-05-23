"""
描述器实现ORM模型中的字段类型
字符串类型字段
int类型字段
布尔字段

可以用描述器简单实现ORM模型字段，
但是ORM模型并不是这么实现的,ORM模型是利用元类实现的
"""


# str 字段
class CharField:
    """
    设置一个str属性值，别的类在引用这个描述器
    给属性赋值的时候限定了属性类型为str
    """

    # 传入字符串长度
    def __init__(self, max_length=20):
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_length:
                self.value = value
            else:
                raise ValueError("str Length should not exceed {}".format(self.max_length))
        else:
            raise TypeError("Must be a string type not{}".format(type(value)))

    def __delete__(self, instance):
        self.value = None


# int字段
class IntField:
    """
    设置一个Int属性值，别的类在引用这个描述器
    给属性赋值的时候限定了属性类型为int
    """

    # 传入字符串长度
    def __init__(self, max_value=40):
        self.max_value = max_value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            if value <= self.max_value:
                self.value = value
            else:
                raise ValueError("The value should not be greater than  {}".format(self.max_value))
        else:
            raise TypeError("Must be a int type not{}".format(type(value)))

    def __delete__(self, instance):
        self.value = None


# 布尔类型
class BooleanField:
    """
    设置一个Bool属性值，别的类在引用这个描述器
    给属性赋值的时候限定了属性类型为Bool
    """

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):
            self.value = value
        else:
            raise TypeError("%s  Not Boolean " % type(value))

    def __delete__(self, instance):
        self.value = None


class UserModel:
    # 设置描述其类的属性 字符串类型
    # 假设我这个是模型类
    name = CharField(max_length=20)
    paw = CharField(max_length=40)
    age = IntField(30)
    status = BooleanField()


m = UserModel()
# 赋值字符串类型
m.name = "999"
# m.paw = "sfsdfsfsdfasfsadfsdafsdsfasffsfasfdsafsdfsafs"  # 超长为空
print(m.name)  # 可以设置字符串类型
# m.name = 123  # 设置非字符串类型报错

# 赋值int
m.age = 18
# m.age = 60 # 超大报错
# m.age = "111"  # 类型报错

# 布尔类型
m.status = False
# m.status = 111  # 类型报错
