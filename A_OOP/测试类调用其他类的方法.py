
# 非测试类
class cltdy:  # 定义类，并起一个名字
    n = 1000  # 类属性，类内的变量

    def __init__(self, age, profession='IT民工'):  # 构造函数，类接收外部传入参数全靠构造函数
        self.name = 111
        self.age = age
        self.profession = profession

    def printing_name(self):  # 类的方法
        print('我的名字是：%s' % self.name)

    def printing_age(self):
        print("我的年龄：%s" % self.age)

    def printing_pfsn(self):
        print("我的职业：%s" % self.profession)

# 【测试类】中，调用【其他类】的方法，方法中调用了类属性
class TestClass1:
    def test_Case1(self):
        print(cltdy(25, 'DevOps').printing_name())