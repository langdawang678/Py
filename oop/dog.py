"""
1、类的声明
2、实例化（初始化）
3、self的含义
4、类属性（类里&方法体之外）：
    通过类里或者对象调用
    （修改只能在类里，即类.属性=新的属性值）
5、类方法（类里定义的方法）：
    外部，只能对象调用
    内部，类里的方法调用其他方法，要用self去调用
6、实例属性（对象的属性）：
    在__init__中定义，对象名调用和修改
"""

# 定义一个狗类
class Dog:
    dog_common = "lovely"  # 类属性，类里或者对象调用

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.dog_name = name
        self.age = age
        print('打印__init__()中的self：', self)  # 1、self在类的定义中，表示对象自己。
        # 2、即初始化时my_dog调用了__init__函数，此时self打印，等于my_dog的打印。your_dog同理

    def sit(self):  # 类方法，只能对象调用
        print(self.dog_name + " is now sitting.")

    def roll_over(self):
        print(self.dog_name + " rolled over!")
        self.sit()  # 类里的方法调用其他方法，要用self去调用（用类名去调用不规范）
    # print(dog_common)  # lovely

# 根据类创建实例my_dog
my_dog = Dog('小白', 6)
print(f"{my_dog.dog_name} is {my_dog.age} years old.")
print(my_dog.dog_common)  # lovely ,类属性的作用域在类中，即只能类中或者类的对象调用（区别于全局变量）
my_dog.sit()
print("打印对象my_dog：", my_dog, "\n")  # 等于__init__()函数中打印的self

# 根据类创建实例your_dog
your_dog = Dog('大黑', 3)
print("打印对象your_dog：", your_dog)  # 等于__init__()函数中打印的self
