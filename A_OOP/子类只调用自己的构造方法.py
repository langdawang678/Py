class A:
    def __init__(self):
        print("A的初始化方法")
        self.nameA = "nameA"

    def methodA(self):
        print(f"A的类方法，调用父类A的类变量：{self.nameA}")


# B没有自己的初始化方法，就用父类A的
class B(A):
    # def __init__(self):
    #     print("B的初始化方法")
    pass


class C(A):
    # C有自己的初始化方法，就用自己的
    def __init__(self):
        print("C的初始化方法")


# 子类调用父类的属性
class D(A):
    @property
    def getNameFromA(self):
        print("D的初始化方法", f"调用父类A的类变量：{self.nameA}")


if __name__ == '__main__':
    A().methodA()  # A的初始化方法， A的类方法，调用父类A的类变量：nameA
    B()  # A的初始化方法
    C()  # C的初始化方法
    D().getNameFromA  # A的初始化方法， D的初始化方法 调用父类A的类变量：nameA
