"""
实例方法：self,用的最多。
        调用：self.  obj.
静态方法 @staticmethod：有提示的时候改为@staticmethod
        没有self的方法，理解为放在类下面的普通函数，为了方便代码管理
        调用：self.  obj. 类名.
类方法 @classmethod：用来做备用的构造函数。一般很少用到。
        cls代表类本身
        调用：类. 实例.
"""
class Dalao:
    favor = "python"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat(food):
        print(f"大佬喜欢吃{food}")
        return f"大佬喜欢吃{food}"

    def offer(self, monkey, food):
        print(f"恭喜{self.name}拿到{monkey}的offer")
        food = self.eat(food)
        Dalao.code()

    @classmethod
    def code(cls):
        dalao = Dalao("四叶草")
        print(f"我喜欢的编程语言是{cls.favor}")

    @classmethod
    def make_instance(cls, name):
        return cls(name)

dalao = Dalao("克拉美学")
dalao.offer("40k","辣条")
Dalao.eat("辣条")

dalao.code()
