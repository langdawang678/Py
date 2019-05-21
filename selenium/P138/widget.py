class Widget:
    def __init__(self, size=(40, 40)):
        self._size = size

    def getSize(self):
        return self._size

    def reSize(self, width, height):
        if width < 0 or height < 0:
            raise ValueError, "illegal size"
        self._size = (width, height)

    def dispose(self):
        pass

''' 
a.__init__()方法在类的一个对象被建立时，马上运行。这个方法可以用来对你的对象做一些你希望的初
始化
b.如果要将一个方法声明为 private 的，只要在方法名前面加上“ __ ”即可。
c.在类的方法中必须有个额外的第一个参数（self），但在调用类的方法时却不必为这个参数赋值。self 参数所指的是对象本身，所以习惯
性地命名为 self
'''


