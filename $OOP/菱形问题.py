"""
菱形问题：演示多继承和交叉继承时，子类的查找顺序。
（A在顶部。BC继承A。D在底部，继承BC。修改点：C是否继承A）
    1、广度优先，
    2、深度优先，
    *3、c3算法，现在的Python是C3算法，以前的版本是深度，更早是广度。
        会根据菱形里的C是否继承A，来自动判断是广度还是深度优先。
print(D.__mro__)  # 显示顺序
"""

class A:
    def play(self):
        print("a is playing")
    pass


class B(A):
    # def play(self):
    #     print("b is playing")
    pass


class C(A):   # 广度优先，调用C，（记忆：加了A反而不调用）
    # class C: # 深度优先，调用B的父类A
    def play(self):
        print("c is playing")
    pass


class D(B, C):
    # def play(self):
    #     print("d is playing")
    pass

d = D()
d.play()
print(f"完整菱形时，D的查找顺序：{D.__mro__}")
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
